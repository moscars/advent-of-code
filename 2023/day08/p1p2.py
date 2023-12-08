from math import gcd

class Ghost:
    def __init__(self, pos):
        self.pos = pos
        self.target = None
        self.toTargetDist = None
        self.targetToTargetDist = None
    
lines = open(0).read().splitlines()

directions = lines[0]
mp = {}
ghosts = []

for line in lines[2:]:
    f, s = line.split(" = ")
    l, r = s.split(", ")
    mp[f] = (l[1:], r[:-1])
    if f[-1] == 'A':
        ghosts.append(Ghost(f))

def findDist(curr, to_):
    idx = 0
    ans = 0
    while idx == 0 or (len(to_) == 3 and curr != to_) or (len(to_) == 1 and curr[-1] != to_):
        if idx >= len(directions):
            idx = 0

        if directions[idx] == 'R':
            curr = mp[curr][1]
        else:
            curr = mp[curr][0]

        idx += 1
        ans += 1
    
    to_ = curr

    return ans, to_

lcm = 1
for ghost in ghosts:
    # found through simulation that all ghosts only encounter one 'Z' location
    dist, target = findDist(ghost.pos, 'Z')
    ghost.target = target
    ghost.toTargetDist = dist
    ghost.targetToTargetDist, _ = findDist(target, target)

    # the distance to the target is the same as the length of the loop so we can just use lcm. 
    # didn't see this at first, so used the chinese remainder theorem with non-coprime moduli during the contest.
    assert ghost.targetToTargetDist == ghost.toTargetDist, f"{ghost.targetToTargetDist} {ghost.toTargetDist}"
    lcm = lcm * ghost.targetToTargetDist // gcd(lcm, ghost.targetToTargetDist)

print(findDist('AAA', 'ZZZ')[0])
print(lcm)