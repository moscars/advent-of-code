from collections import deque
lines = open(0).read().splitlines()

cubes = []
for line in lines:
    x, y, z = map(int, line.split(','))
    cubes.append((x, y, z))

cubeSet = set(cubes)

def adjacent(cube):
    x, y, z = cube
    return [
        (x, y, z+1),
        (x, y, z-1),
        (x, y+1, z),
        (x, y-1, z),
        (x+1, y, z),
        (x-1, y, z)]

maxLim = max(val for cube in cubes for val in cube) + 3
minLim = min(val for cube in cubes for val in cube) - 3
def inBounds(cube):
    x, y, z = cube
    return minLim <= x <= maxLim and minLim <= y <= maxLim and minLim <= z <= maxLim

q = deque()
seen = set()
q.append((maxLim - 1, maxLim - 1, maxLim - 1))
while len(q) > 0:
    cube = q.popleft()

    if cube in seen or cube in cubeSet: continue
    seen.add(cube)

    for neigh in adjacent(cube):
        if inBounds(neigh):
            q.append(neigh)

p1, p2 = 0, 0
for cube in cubes:
    for neigh in adjacent(cube):
        if neigh not in cubeSet:
            p1 += 1
            if neigh in seen:
                p2 += 1
print(p1)
print(p2)