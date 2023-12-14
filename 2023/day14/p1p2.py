from copy import deepcopy

lines = open(0).read().splitlines()
g = [[c for c in line] for line in lines]

def rollNorth(g):
    newG = deepcopy(g)
    for j in range(len(g[0])):
        restingPlace = 0
        for i in range(len(g)):
            if g[i][j] == "O":
                newG[i][j] = "."
                newG[restingPlace][j] = "O"
                restingPlace += 1
            elif g[i][j] == "#":
                restingPlace = i + 1
    return newG

def getNorthPressure(g):
    p = 0
    for i in range(len(g)):
        p += g[i].count("O") * (len(g) - i)
    return p

def rotate90(g):
    g = map(list, zip(*g))
    g = list(map(lambda x: x[::-1], g))
    return g

def rollAll(g):
    g = list(map(list, g))
    g = rollNorth(g)
    g = rollNorth(rotate90(g))
    g = rollNorth(rotate90(g))
    g = rollNorth(rotate90(g))
    g = rotate90(g)
    g = tuple(map(tuple, g))
    return g

seen = {}
i = 0
startG = deepcopy(g)
g = tuple(map(tuple, g))
while g not in seen:
    if g not in seen:
        seen[g] = i
    g = rollAll(g)
    i += 1

cycleLength = i - seen[g]
itersNeeded = (int(1e9) - seen[g]) % cycleLength
for _ in range(itersNeeded):
    g = rollAll(g)

print(f"Part 1: {getNorthPressure(rollNorth(startG))}")
print(f"Part 2: {getNorthPressure(g)}")