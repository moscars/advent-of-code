import re
data = open(0).read()
gg, code = data.split("\n\n")

grid = [[c for c in row] for row in gg.split('\n')]

maxWidth = max([len(row) for row in grid])
for i in range(len(grid)):
    while len(grid[i]) < maxWidth:
        grid[i].append(' ')

firstHor = [min([j for j in range(len(grid[i])) if grid[i][j] != ' ']) for i in range(len(grid))]
lastHor = [max([j for j in range(len(grid[i])) if grid[i][j] != ' ']) for i in range(len(grid))]
firstVert = [min([i for i in range(len(grid)) if grid[i][j] != ' ']) for j in range(len(grid[0]))]
lastVert = [max([i for i in range(len(grid)) if grid[i][j] != ' ']) for j in range(len(grid[0]))]

y = 0
x = min([j for j in range(len(grid[0])) if grid[0][j] == '.'])

dirr = 0
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
actions = re.findall(r'\d+|\D', code)

def move(x, y, dx, dy):
    x += dx
    y += dy
    if dx != 0 and x > lastHor[y]:
        return firstHor[y], y
    elif dx != 0 and x < firstHor[y]:
        return lastHor[y], y
    elif dy != 0 and y > lastVert[x]:
        return x, firstVert[x]
    elif dy != 0 and y < firstVert[x]:
        return x, lastVert[x]
    return x, y

for action in actions:
    if action == 'L':
        dirr = (dirr - 1) % 4
    elif action == 'R':
        dirr = (dirr + 1) % 4
    else:
        dx, dy = dirs[dirr]
        for i in range(int(action)):
            x, y = move(x, y, dx, dy)
            if grid[y][x] == '#':
                x, y = move(x, y, -dx, -dy)
                break

print((y + 1) * 1000 + (x + 1) * 4 + dirr)
