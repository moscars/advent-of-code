from math import lcm

lines = open(0).read().splitlines()

directions = lines[0]
mp = {}

for line in lines[2:]:
    f, s = line.split(" = ")
    l, r = s.split(", ")
    mp[f] = (l[1:], r[:-1])

def findDist(curr, to_):
    ans = 0
    while ans == 0 or (len(to_) == 3 and curr != to_) or (len(to_) == 1 and curr[-1] != to_):
        if directions[ans % len(directions)] == 'R':
            curr = mp[curr][1]
        else:
            curr = mp[curr][0]
        ans += 1
    
    return ans, curr

ans = 1

ghosts = [pos for pos in mp if pos[-1] == 'A']
for ghost in ghosts:
    # found through simulation that all ghosts only encounter one 'Z' location
    dist, target = findDist(ghost, 'Z')
    targetToTargetDist, _ = findDist(target, target)

    # the distance to the target is the same as the length of the loop so we can just use lcm. 
    # didn't see this at first, so used the chinese remainder theorem with non-coprime moduli during the contest.
    assert targetToTargetDist == dist
    ans = lcm(ans, dist)

print(f"Part 1: {findDist('AAA', 'ZZZ')[0]}")
print(f"Part 2: {ans}")