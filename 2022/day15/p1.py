lines = open(0).read().splitlines()

def mannhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

notPossible = set()
occupied = set()
close = []
for line in lines:
    space = line.split()
    sx = int(space[2].split('=')[1][:-1])
    sy = int(space[3].split('=')[1][:-1])
    bx = int(space[8].split('=')[1][:-1])
    by = int(space[9].split('=')[1])
    close.append([sx, sy, bx, by])
    occupied.add((sx, sy))
    occupied.add((bx, by))

for sx, sy, bx, by in close:
    beaconDist = mannhattan(sx, sy, bx, by)

    y = 2000000
    x = sx
    while mannhattan(sx, sy, x, y) <= beaconDist:
        if not (x, y) in occupied: notPossible.add(x)
        x += 1
    x = sx
    while mannhattan(sx, sy, x, y) <= beaconDist:
        if not (x, y) in occupied: notPossible.add(x)
        x -= 1

print(len(notPossible))