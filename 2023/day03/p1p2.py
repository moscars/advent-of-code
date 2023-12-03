
lines = open(0).read().splitlines()

g = [[c for c in line] for line in lines]

def getNeighs(i, j):
    return [(i+1, j), (i-1, j), (i, j+1), (i, j-1), (i+1, j+1), (i-1, j-1), (i+1, j-1), (i-1, j+1)]

def inBounds(i, j):
    return i >= 0 and i < len(g) and j >= 0 and j < len(g[0])

def adjacentToSymbol(i, j):
    neighs = getNeighs(i, j)
    for ii, jj in neighs:
        if inBounds(ii, jj):
            if not g[ii][jj].isdigit() and g[ii][jj] != ".":
                return True
    return False

def getNum(i, j):
    while j >= 0 and g[i][j].isdigit():
        j -= 1
    j += 1

    num = ""
    locs = set()
    while j < len(g[0]) and g[i][j].isdigit():
        num += g[i][j]
        locs.add((i, j))
        j += 1
    return int(num), locs

def hasTwoNeighs(i, j):
    neighs = getNeighs(i, j)
    seen = set()
    nums = []
    for ii, jj in neighs:
        if inBounds(ii, jj):
            if g[ii][jj].isdigit():
                num, locs = getNum(ii, jj)

                if not any(loc in seen for loc in locs):
                    nums.append(num)
                    seen |= locs

    return nums[0] * nums[1] if len(nums) == 2 else 0

def processNum(i, j):
    locations = set()
    num = ""
    while j < len(line) and line[j].isdigit():
        locations.add(j)
        num += line[j]
        j += 1

    for j in locations:
        if adjacentToSymbol(i, j):
            return int(num), locations
        
    return 0, locations

p1, p2 = 0, 0
for i, line in enumerate(lines):
    used = set()
    for j in range(len(line)):
        if line[j] == "*":
            p2 += hasTwoNeighs(i, j)
        elif line[j].isdigit() and j not in used:
            num, locs = processNum(i, j)
            p1 += num
            used |= locs

print(p1)
print(p2)