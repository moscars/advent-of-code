import math
lines = []

with open('input.in') as f:
    lines = f.readlines()
grid = []

def paddInput():
    global grid
    grid = []
    l = len(lines[3].strip())
    size = 0.7
    paddingSize = int(math.ceil(size * l))

    padding = ""
    for _ in range(paddingSize):
        padding += "."

    midPadding = ""
    for _ in range(l):
        midPadding += "."

    for _ in range(paddingSize):
        r = padding + midPadding + padding
        grid.append(r)

    for i in range(2, len(lines)):
        line = lines[i].strip()
        line = padding + line + padding
        grid.append(line)

    for _ in range(paddingSize):
        r = padding + midPadding + padding
        grid.append(r)

    
def solve(iters):
    global grid
    paddInput()
    code = lines[0].strip()
    for k in range(iters):
        out = [["." for _ in range(len(row))] for row in grid]
        
        for i in range(2, len(grid) - 2):
            for j in range(2, len(grid[0]) - 2):
                sign = grid[i-1][j-1:j+2]
                sign += grid[i][j-1:j+2]
                sign += grid[i+1][j-1:j+2]
                num = ["0" if char == "." else "1" for char in sign]
                index = int("0b" + ''.join(num), 2)
                out[i][j] = code[index]
        
        edges = [0, 1, len(grid) - 1, len(grid) - 2]
        if k % 2 == 0:
            for i in range(len(grid)):
                for edgeVal in edges:
                    out[edgeVal][i] = "#"
                    out[i][edgeVal] = "#"
                    
        grid = out

    return sum(row.count("#") for row in grid)

print(solve(2))
print(solve(50))