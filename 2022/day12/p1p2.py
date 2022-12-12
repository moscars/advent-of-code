from collections import deque

lines = open(0).read().splitlines()
graph = [[c for c in line] for line in lines]
R, C = len(graph), len(graph[0])

def diff(curr, nex, p2=False):
    if p2: 
        return ord(curr) - ord(nex) <= 1
    return ord(nex) - ord(curr) <= 1

def findLocation(c):
    for i in range(R):
        for j in range(C):
            if graph[i][j] == c:
                return i, j

def bfs(starti, startj, goali=None, goalj=None):
    queue = deque()
    seen = set()
    queue.append((starti, startj, 0))
    while len(queue) > 0:
        i, j, steps = queue.popleft()

        if (goali is None and graph[i][j] == 'a') or (i == goali and j == goalj):
            return steps
        if (i, j) in seen: continue
        seen.add((i, j))

        neighs = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
        for ni, nj in neighs:
            if 0 <= ni < R and 0 <= nj < C and diff(graph[i][j], graph[ni][nj], goali is None):
                queue.append((ni, nj, steps + 1))

iS, jS = findLocation('S')
iE, jE = findLocation('E')
graph[iS][jS] = 'a'
graph[iE][jE] = 'z'
print(bfs(iS, jS, iE, jE))
print(bfs(iE, jE))