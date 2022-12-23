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

dirr = 0
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
actions = re.findall(r'\d+|\D', code)

SIDELEN = 50
blocks = []
for horizDiff in range(3):
    for vertDiff in range(4):
        block = []
        for i in range(SIDELEN):
            row = []
            for j in range(SIDELEN):
                row.append(grid[vertDiff * SIDELEN + i][horizDiff * SIDELEN + j])
            block.append(row)
        blocks.append(block)

blocks = list(filter(lambda block: block[0][0] != ' ', blocks))

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

upIndex, downIndex, leftIndex, rightIndex = {}, {}, {}, {}

upIndex[0] = (3, RIGHT)
downIndex[0] = (1, DOWN)
leftIndex[0] = (2, RIGHT)
rightIndex[0] = (4, RIGHT)

upIndex[1] = (0, UP)
downIndex[1] = (5, DOWN)
leftIndex[1] = (2, DOWN)
rightIndex[1] = (4, UP)

upIndex[2] = (1, RIGHT)
downIndex[2] = (3, DOWN)
leftIndex[2] = (0, RIGHT)
rightIndex[2] = (5, RIGHT)

upIndex[3] = (2, UP)
downIndex[3] = (4, DOWN)
leftIndex[3] = (0, DOWN)
rightIndex[3] = (5, UP)

upIndex[4] = (3, UP)
downIndex[4] = (1, LEFT)
leftIndex[4] = (0, LEFT)
rightIndex[4] = (5, LEFT)

upIndex[5] = (1, UP)
downIndex[5] = (3, LEFT)
leftIndex[5] = (2, LEFT)
rightIndex[5] = (4, LEFT)

def inv(val):
    return SIDELEN - 1 - val

def up(blockIndex, x, y):
    newIndex, dirr = upIndex[blockIndex]
    nx, ny = 0, 0
    if dirr == UP:
        nx, ny = x, SIDELEN - 1
    elif dirr == LEFT:
        nx, ny = SIDELEN - 1, inv(x)
    elif dirr == RIGHT:
        nx, ny = 0, x
    elif dirr == DOWN:
        nx, ny = inv(x), 0
    return nx, ny, dirr, newIndex
    
def down(blockIndex, x, y):
    newIndex, dirr = downIndex[blockIndex]
    nx, ny = 0, 0
    if dirr == UP:
        nx, ny = inv(x), SIDELEN - 1
    elif dirr == LEFT:
        nx, ny = SIDELEN - 1, x
    elif dirr == RIGHT:
        nx, ny = 0, inv(y)
    elif dirr == DOWN:
        nx, ny = x, 0
    return nx, ny, dirr, newIndex

def left(blockIndex, x, y):
    newIndex, dirr = leftIndex[blockIndex]
    nx, ny = 0, 0
    if dirr == UP:
        nx, ny = inv(y), SIDELEN - 1
    elif dirr == LEFT:
        nx, ny = SIDELEN - 1, y
    elif dirr == RIGHT:
        nx, ny = 0, inv(y)
    elif dirr == DOWN:
        nx, ny = y, 0
    return nx, ny, dirr, newIndex

def right(blockIndex, x, y):
    newIndex, dirr = rightIndex[blockIndex]
    nx, ny = 0, 0
    if dirr == UP:
        nx, ny = y, SIDELEN - 1
    elif dirr == LEFT:
        nx, ny = SIDELEN - 1, inv(y)
    elif dirr == RIGHT:
        nx, ny = 0, y
    elif dirr == DOWN:
        nx, ny = inv(y), 0
    return nx, ny, dirr, newIndex

def move(x, y, dirr, blockIndex):
    if dirr == UP:
        if y == 0:
            return up(blockIndex, x, y)
        else:
            return x, y - 1, dirr, blockIndex, 
    elif dirr == DOWN:
        if y == SIDELEN - 1:
            return down(blockIndex, x, y)
        else:
            return x, y + 1, dirr, blockIndex
    elif dirr == LEFT:
        if x == 0:
            return left(blockIndex, x, y)
        else:
            return x - 1, y, dirr, blockIndex
    elif dirr == RIGHT:
        if x == SIDELEN - 1:
            return right(blockIndex, x, y)
        else:
            return x + 1, y, dirr, blockIndex

blockOffset = {
    0: {'y': 100, 'x': 0},
    1: {'y': 150, 'x': 0},
    2: {'y': 0, 'x': 50},
    3: {'y': 50, 'x': 50},
    4: {'y': 100, 'x': 50},
    5: {'y': 0, 'x': 100},
}

y, blockIndex = 0, 2
x = min([j for j in range(len(blocks[2][0])) if blocks[2][0][j] == '.'])

for action in actions:
    if action == 'L':
        dirr = (dirr - 1) % 4
    elif action == 'R':
        dirr = (dirr + 1) % 4
    else:
        for i in range(int(action)):
            old = (x, y, dirr, blockIndex)
            x, y, dirr, blockIndex = move(x, y, dirr, blockIndex)
            if blocks[blockIndex][y][x] == '#':
                x, y, dirr, blockIndex = old
                break

print((y + 1 + blockOffset[blockIndex]['y']) * 1000 + (x + 1 + blockOffset[blockIndex]['x']) * 4 + dirr)
