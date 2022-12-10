import numpy as np

lines = []

with open('input.in') as f:
    lines = f.readlines()

scanners = {}
scanner = -1
for line in lines:
    line = line.strip()
    if len(line) >= 17:
        scanner += 1
        scanners[scanner] = []
    else:
        if len(line) > 2:
            nums = [int(x) for x in line.split(",")]
            scanners[scanner].append(nums)

def getAdjusted(point, rot):
    out = [0] * 3
    for i, r in enumerate(rot):
        out[i] = point[abs(r) - 1] * (-1 if r < 0 else 1) 
    return out

def getAdjustedPoints(points, rot):
    out = []
    for p in points:
        out.append(getAdjusted(p, rot))
    return out

def adjustPointsGivenPos(pos, points):
    x = pos[0]
    y = pos[1]
    z = pos[2]
    new = []
    for p in points:
        new.append([x + p[0], y + p[1], z + p[2]])
    return new

def generateRots():
    ret = []
    for x in range(-3, 4):
        for y in range(-3, 4):
            for z in range(-3, 4):
                if x == 0 or y == 0 or z == 0:
                    continue
                if abs(x) == abs(y) or abs(x) == abs(z) or abs(z) == abs(y):
                    continue
                
                row1 = [0, 0, 0]
                row1[abs(x) - 1] = 1 if x > 0 else -1
                row2 = [0, 0, 0]
                row2[abs(y) - 1] = 1 if y > 0 else -1
                row3 = [0, 0, 0]
                row3[abs(z) - 1] = 1 if z > 0 else -1
                
                ar = np.array([row1, row2, row3])
                det = np.linalg.det(ar)
                if int(det) > 0:
                    ret.append([x, y, z])
    return ret

def getMatches(points0, points1):
    global poss
    global total
    matchedPoints = set()
    pos = [0, 0, 0]
    for i in range(len(points0)):
        for j in range(len(points0)):
            if i == j:
                continue
            xdist = points0[i][0] - points0[j][0]
            ydist = points0[i][1] - points0[j][1]
            zdist = points0[i][2] - points0[j][2]
            matchHere = False
            for k in range(len(points1)):
                if matchHere:
                    break
                for k2 in range(len(points1)):
                    if k == k2:
                        continue
                    xdist2 = points1[k][0] - points1[k2][0]
                    ydist2 = points1[k][1] - points1[k2][1]
                    zdist2 = points1[k][2] - points1[k2][2]
                    if xdist == xdist2 and ydist == ydist2 and zdist == zdist2:
                        pos[0] = points0[i][0] - points1[k][0]
                        pos[1] = points0[i][1] - points1[k][1]
                        pos[2] = points0[i][2] - points1[k][2]
                        matchedPoints.add((points0[i][0], points0[i][1], points0[i][2]))
                        matchedPoints.add((points0[j][0], points0[j][1], points0[j][2]))
                        matchHere = True
                        break
    if len(matchedPoints) >= 12:
        poss.append(pos)
        return (True, pos)
    return (False, pos)  

rotations = generateRots()
total = []
searching = 0
poss = []

for p in scanners[0]:
    total.append(p)
    
stack = []
stack.append(0)
considered = {}
doneRotations = {}
doneRotations[0] = [1, 2, 3]
for i in range(len(scanners)):
    considered[i] = set()

while len(stack) > 0:
    seeker = stack.pop()
    for sc in range(len(scanners)):
        if sc in considered[seeker] or seeker in considered[sc] or sc == seeker:
            continue
        considered[seeker].add(sc)
        considered[sc].add(seeker)
        points = scanners[sc]
        for rot in rotations:
            if sc in doneRotations:
                rot = doneRotations[sc]
            p = getAdjustedPoints(points, rot)
            enough, pos = getMatches(scanners[seeker], p)
            if enough:
                newPoints = adjustPointsGivenPos(pos, p)
                doneRotations[sc] = rot
                print("match between scanners " + str(seeker) + " and " + str(sc))
                for p in newPoints:
                    if p not in total:
                        total.append(p)
                scanners[sc] = newPoints
                if sc not in stack:
                    stack.append(sc)
                break
            if sc in doneRotations:
                break

maxx = 0
for i in range(len(poss)):
    for j in range(i+1, len(poss)):
        if i == j:
            continue
        potential = 0
        for k in range(3):
            potential += abs(poss[i][k] - poss[j][k])
        if potential > maxx:
            maxx = potential
            
print(len(total))
print(maxx)