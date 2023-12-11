
graph = open(0).read().splitlines()

def getJumps(graph):
    jumps = []
    for i, line in enumerate(graph):
        if "#" not in line:
            jumps.append(i)
    return jumps

rowJumps = getJumps(graph)
colJumps = getJumps(list(map(list, zip(*graph))))

locations = []
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == "#":
            locations.append((i, j))

p1, p2 = 0, 0
for i in range(len(locations)):
    for j in range(i + 1, len(locations)):
        
        rowExpand = 0
        for jump in rowJumps:
            if locations[j][0] < jump < locations[i][0] or locations[i][0] < jump < locations[j][0]:
                rowExpand += 1
        
        colExpand = 0
        for jump in colJumps:
            if locations[j][1] < jump < locations[i][1] or locations[i][1] < jump < locations[j][1]:
                colExpand += 1
        
        distanceP1 = rowExpand + colExpand
        distanceP2 = rowExpand * (1_000_000 - 1) + colExpand * (1_000_000 - 1)
        realDist = abs(locations[i][0] - locations[j][0]) + abs(locations[i][1] - locations[j][1])

        p1 += distanceP1 + realDist
        p2 += distanceP2 + realDist

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")