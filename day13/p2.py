
lines = []

with open('input.in') as f:
    lines = f.readlines()

dots = []
folds = []

f = False
maxX = 0
maxY = 0
for line in lines:
    d = line.strip()
    if d == "":
        f = True
        continue
    if f:
        folds.append(d)
    else:
        x, y = line.split(",")
        x = int(x)
        y = int(y)
        if x > maxX: maxX = x
        if y > maxY: maxY = y
        dots.append((x, y))


grid = [[" " for _ in range(maxX + 1)] for _ in range(maxY + 1)]

for dot in dots:
    x, y = dot
    grid[y][x] = "#"

for fold in folds:
    fold = fold.split()[2]
    dirr, val = fold.split("=")
    val = int(val)

    if dirr == "y":
        for row in range(val+1, len(grid)):
            for x in range(len(grid[row])):
                if grid[row][x] == "#":
                    grid[val - abs(val - row)][x] = "#"
                    
        ng = [[elem for elem in grid[y]] for y in range(val + 1)]
        grid = ng
        
    else:
        for y in range(len(grid)):
            for x in range(val + 1, len(grid[y])):
                if grid[y][x] == "#":
                    grid[y][val - abs(val - x)] = "#"
        
        ng = [[grid[y][x] for x in range(val)] for y in range(len(grid))]
        grid = ng
        
for row in grid:
    print(''.join(row))

            
            
        