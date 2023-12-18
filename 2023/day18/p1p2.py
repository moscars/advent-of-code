
lines = open(0).read().splitlines()

mp = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0)
}

lastMp = {
    '0': 'R',
    '1': 'D',
    '2': 'L',
    '3': 'U'
}

insP1 = []
insP2 = []
for line in lines:
    di, num, code = line.split()
    insP1.append((di, int(num)))

    code = code[2:-1]
    insP2.append((lastMp[code[-1]], int(code[:-1], 16)))

def getPolygon(instructions):
    loc = (0, 0)
    polygon = []
    gSize = 0
    for d, num in instructions:
        new_loc = (loc[0] + mp[d][0] * num, loc[1] + mp[d][1] * num)
        gSize += abs(new_loc[0] - loc[0]) + abs(new_loc[1] - loc[1])
        polygon.append(new_loc)
        loc = new_loc

    return polygon, gSize

def cross(p1, p2):
    return p1[0] * p2[1] - p1[1] * p2[0]

def polygonArea(polygon):
    area = 0
    n = len(polygon)
    for i in range(n):
        area += cross(polygon[i], polygon[(i+1)%n])
    return abs(area) // 2

def solve(instructions):
    polygon, gSize = getPolygon(instructions)
    area = polygonArea(polygon)
    return area + gSize - (gSize - 2) // 2

print(f"Part 1: {solve(insP1)}")
print(f"Part 2: {solve(insP2)}")