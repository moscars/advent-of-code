
lines = open(0).read().splitlines()

graph = [[int(v) for v in row] for row in lines]
R = len(graph)
C = len(graph[0])

def getViewinDir(val, i, j, di, dj):
    dist = 0
    while 0 <= i + di < R and 0 <= j + dj < C:
        i += di
        j += dj
        dist += 1
        if graph[i][j] >= val: 
            return False, dist
    return True, dist

def visible(val, i, j):
    for di, dj in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
        if getViewinDir(val, i, j, di, dj)[0]:
            return True
    return False

def scenic(val, i, j):
    product = 1
    for di, dj in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
        product *= getViewinDir(val, i, j, di, dj)[1]
    return product

p1 = 0
p2 = 0
for i in range(len(graph)):
    for j in range(len(graph[0])):
        p1 += visible(graph[i][j], i, j)
        p2 = max(p2, scenic(graph[i][j], i, j))

print(p1)
print(p2)