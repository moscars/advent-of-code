from collections import deque

data = open(0).read().splitlines()
grid = [list(line) for line in data]
R, C = len(grid), len(grid[0])

blizzards = [set() for _ in range(4)]
signs = ['>', '<', '^', 'v']
diff = [(0, 1), (0, -1), (-1, 0), (1, 0)]
wrap = {
    0: lambda i, j: (i, 1),
    1: lambda i, j: (i, C - 2),
    2: lambda i, j: (R - 2, j),
    3: lambda i, j: (1, j)
}

for i in range(R):
    for j in range(C):
        if grid[i][j] in signs:
            blizzards[signs.index(grid[i][j])].add((i, j))

def nextGrid(blizzards):
    newBlizzards = [set() for _ in range(4)]
    for index in range(4):
        for i, j in blizzards[index]:
            ni, nj = i + diff[index][0], j + diff[index][1]
            if grid[ni][nj] != '#':
                newBlizzards[index].add((ni, nj))
            else:
                newBlizzards[index].add(wrap[index](i, j))
    return newBlizzards

free = []
for _ in range(1000):
    currSet = set()
    for i in range(R):
        for j in range(C):
            if grid[i][j] == '#' or any([(i, j) in blizzards[index] for index in range(4)]):
                continue
            currSet.add((i, j))
    free.append(currSet)
    blizzards = nextGrid(blizzards)

def canMove(i, j, depth):
    if i < 0 or j < 0 or i >= R or j >= C: 
        return False
    
    if (i, j) not in free[depth]:
        return False
    return True

q = deque()
seen = set()
q.append((0, 1, 0, 1))
p1 = 0
while len(q):
    state = i, j, depth, goal = q.popleft()

    if i == R - 1 and j == C - 2 and goal == 3:
        print(depth)
        exit(0)
    if i == 0 and j == 1 and goal == 2:
        goal = 3
    if i == R - 1 and j == C - 2 and goal == 1:
        if p1 == 0:
            p1 = depth
            print(p1)
        goal = 2

    if state in seen: continue
    seen.add(state)

    neighs = [(i+1, j), (i-1, j), (i, j+1), (i, j-1), (i, j)]
    for ii, jj in neighs:
        if canMove(ii, jj, depth + 1):
            q.append((ii, jj, depth + 1, goal))