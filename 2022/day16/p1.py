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

minutes, value, best, prevBest = 1, 0, 0, 0
openedPlaces, seen = set(), set()
def backtrack(curr):
    global value, minutes, best, prevBest
    if(curr, minutes, value) in seen:
        return
    seen.add((curr, minutes, value))

    if minutes == 30:
        if best > prevBest:
            prevBest = best
            print("New best:", best)
        best = max(best, value)
        return
    
    # we open this one
    if curr not in openedPlaces:
        openedPlaces.add(curr)
        value += amt[curr] * (30 - minutes)
        minutes += 1
        backtrack(curr)
        minutes -= 1
        value -= amt[curr] * (30 - minutes)
        openedPlaces.remove(curr)

    # we do not open this one
    for neigh in tunnel[curr]:
        minutes += 1
        backtrack(neigh)
        minutes -= 1

backtrack("AA")
print("Answer:", best)