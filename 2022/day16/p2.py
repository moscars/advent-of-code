from collections import defaultdict

lines = open(0).read().splitlines()

amt = defaultdict(int)
tunnel = defaultdict(list)

for line in lines:
    l2 = line.split()
    curr = l2[1]
    flow = int(l2[4].split('=')[1][:-1])
    amt[curr] = flow
    neighs = l2[9:]

    for neigh in neighs:
        if neigh[-1] == ',':
            neigh = neigh[:-1]
        tunnel[curr].append(neigh)

def backtrackOnCurr2(curr, curr2):
    global minutes, value
    openedPlaces.add(curr2)
    value += amt[curr2] * (26 - minutes)
    minutes += 1
    backtrack(curr, curr2)
    minutes -= 1
    value -= amt[curr2] * (26 - minutes)
    openedPlaces.remove(curr2)

minutes, value, best, prevBest = 1, 0, 0, 0
openedPlaces, seen = set(), set()
def backtrack(curr, curr2):
    global minutes, value, best, prevBest

    state = (curr, curr2, minutes, value)
    if state in seen:
        return
    seen.add(state)

    if minutes == 26:
        if best > prevBest:
            prevBest = best
            print("New best:", best)
        best = max(best, value)
        return
    
    if curr == curr2:
        for neigh in tunnel[curr]:
            if curr2 not in openedPlaces and amt[curr2] != 0:
                backtrackOnCurr2(neigh, curr2)

            for neigh2 in tunnel[curr2]:
                minutes += 1
                backtrack(neigh, neigh2)
                minutes -= 1
        return
    
    # we open
    if curr not in openedPlaces and amt[curr] != 0:

        openedPlaces.add(curr)
        value += amt[curr] * (26 - minutes)

        # the other person also opens
        if curr2 not in openedPlaces and amt[curr2] != 0:
            backtrackOnCurr2(curr, curr2)

        # the other person does not open
        for neigh2 in tunnel[curr2]:
            minutes += 1
            backtrack(curr, neigh2)
            minutes -= 1
        
        value -= amt[curr] * (26 - minutes)
        openedPlaces.remove(curr)

    # we do not open
    for neigh in tunnel[curr]:

        # the other person opens
        if curr2 not in openedPlaces and amt[curr2] != 0:
            backtrackOnCurr2(neigh, curr2)

        # the other person does not open
        for neigh2 in tunnel[curr2]:
            minutes += 1
            backtrack(neigh, neigh2)
            minutes -= 1

backtrack("AA", "AA")
print("Answer:", best)