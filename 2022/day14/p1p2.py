
lines = open(0).read().splitlines()

grid = set()
maxY = 0
for line in lines:
    paths = line.split('->')
    px, py = map(int, paths[0].split(','))
    
    for path in paths[1:]:
        cx, cy = map(int, path.split(','))
        for x in range(min(px, cx), max(cx, px) + 1):
            grid.add((x, py))
        for y in range(min(py, cy), max(cy, py) + 1):
            grid.add((px, y))
        px, py = cx, cy
        maxY = max(maxY, py)

floorY = maxY + 2

def fall():
    x, y = 500, 0
    while True:
        if y + 1 == floorY:
            break
        elif (x, y + 1) not in grid:
            x, y = x, y + 1
        elif (x - 1, y + 1) not in grid:
            x, y = x - 1, y + 1
        elif (x + 1, y + 1) not in grid:
            x, y = x + 1, y + 1
        else:
            break
    return x, y

p1, stones = 0, 0
while (500, 0) not in grid:
    x, y = fall()
    if y > maxY and p1 == 0:
        p1 = stones
    grid.add((x, y))
    stones += 1

print(p1)
print(stones)
