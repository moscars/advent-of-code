from copy import deepcopy
from collections import defaultdict

lines = open(0).read().splitlines()

class Brick:
    def __init__(self, x1, y1, z1, x, y, z):
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.x = x
        self.y = y
        self.z = z
    
    def getBelow(self):
        under = []
        if self.z1 != self.z:
            under.append((self.x, self.y, min(self.z, self.z1) - 1))
            return under
        
        for x in range(min(self.x, self.x1), max(self.x, self.x1) + 1):
            for y in range(min(self.y, self.y1), max(self.y, self.y1) + 1):
                under.append((x, y, self.z - 1))
        
        return under
    
    def getLocation(self):
        locs = set()
        for x in range(min(self.x, self.x1), max(self.x, self.x1) + 1):
            for y in range(min(self.y, self.y1), max(self.y, self.y1) + 1):
                for z in range(min(self.z, self.z1), max(self.z, self.z1) + 1):
                    locs.add((x, y, z))
        return locs

bricks = []
occupied = set()
for line in lines:
    x1, y1, z1, x2, y2, z2 = map(int, line.replace('~', ',').split(','))
    b = Brick(x1, y1, z1, x2, y2, z2)
    bricks.append(b)
    occupied |= b.getLocation()

def fall(brickRem, occupied, bricks):
    occu2 = deepcopy(occupied)
    bricks2 = deepcopy(bricks)

    if brickRem is not None:
        occu2 -= brickRem.getLocation()

    fell = True
    allFell = set()
    while fell:
        mp = defaultdict(list)
        for i, brick in enumerate(bricks2):
            mp[min(brick.z, brick.z1)].append(i)

        fell = False
        maMI = max(mp.keys())
        for minZ in range(2, maMI + 1):
            for i in mp[minZ]:
                brick = bricks2[i]

                if any(loc in occu2 for loc in brick.getBelow()):
                    continue
                
                fell = True
                allFell.add(i)
                occu2 -= brick.getLocation()
                brick.z -= 1
                brick.z1 -= 1
                occu2 |= brick.getLocation()

    return len(allFell), bricks2, occu2

_, bricks, occupied = fall(None, occupied, bricks)

p1 = p2 = 0
for i, brick in enumerate(bricks):
    print(f"Processing brick {i+1} of {len(bricks)}")
    numFell, _, _ = fall(brick, occupied, bricks)
    p1 += numFell == 0
    p2 += numFell

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")