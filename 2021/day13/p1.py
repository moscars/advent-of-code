
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


grid = [["." for _ in range(maxX + 1)] for _ in range(maxY + 1)]

for dot in dots:
    x, y = dot
    grid[y][x] = "#"

fold = folds[0]
fold = fold.split()[2]
dirr, val = fold.split("=")
val = int(val)

tot = 0
if dirr == "y":
    for y in range(val+1, len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "#":
                grid[val - abs(val - y)][x] = "#"

    for y in range(val + 1):
        for val in grid[y]:
            if val == "#":
                tot += 1
else:
    for y in range(len(grid)):
        for x in range(val + 1, len(grid[y])):
            if grid[y][x] == "#":
                grid[y][val - abs(val - x)] = "#"
            
    for row in grid:
        for x in range(val):
            if row[x] == "#":
                tot += 1
                
print(tot)

            
            
        