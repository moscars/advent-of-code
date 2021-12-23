lines = []

with open('input.in') as f:
    lines = f.readlines() 

class Cuboid:
    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2

def overlap(c1, c2):
    if c1.x1 > c2.x2 or c1.y1 > c2.y2 or c1.z1 > c2.z2:
        return False
    if c1.x2 < c2.x1 or c1.y2 < c2.y1 or c1.z2 < c2.z1:
        return False
    return True

def removeVolume(cube, volumeToRemove):
    c = cube
    v = volumeToRemove
    
    #create below
    if v.z1 > c.z1:
        cb = Cuboid(c.x1, c.y1, c.z1, c.x2, c.y2, v.z1 - 1)
        totalCubes.append(cb)
        
    #create above
    if c.z2 > v.z2:
        cb = Cuboid(c.x1, c.y1, v.z2+1, c.x2, c.y2, c.z2)
        totalCubes.append(cb)
        
    #create greater than y
    if c.y2 > v.y2:
        cb = Cuboid(c.x1, v.y2+1, max(v.z1, c.z1), c.x2, c.y2, min(v.z2, c.z2))
        totalCubes.append(cb) 
    
    #create less than y
    if v.y1 > c.y1:
        cb = Cuboid(c.x1, c.y1, max(v.z1, c.z1), c.x2, v.y1-1, min(v.z2, c.z2))
        totalCubes.append(cb) 
    
    #create greater than x
    if c.x2 > v.x2:
        cb = Cuboid(v.x2+1, max(v.y1, c.y1), max(v.z1, c.z1), c.x2, min(v.y2, c.y2), min(v.z2, c.z2))
        totalCubes.append(cb) 
    
    #create less than x
    if v.x1 > c.x1:
        cb = Cuboid(c.x1, max(v.y1, c.y1), max(v.z1, c.z1), v.x1-1, min(v.y2, c.y2), min(v.z2, c.z2))
        totalCubes.append(cb)
        
    #remove original
    totalCubes.remove(c)

def addCubiod(cubeToAdd):
    g = [c for c in totalCubes]
    for cube in g:
        if overlap(cube, cubeToAdd):
            removeVolume(cube, cubeToAdd)
    totalCubes.append(cubeToAdd)
    
def removeCuboid(cubeToRemove):
    g = [c for c in totalCubes]
    for cube in g:
        if overlap(cube, cubeToRemove):
            removeVolume(cube, cubeToRemove)
        
def volume(cube):
    return (cube.x2 - (cube.x1 - 1)) * (cube.y2 - (cube.y1 - 1)) * (cube.z2 - (cube.z1 - 1))

def getAns():
    tot = 0
    for cube in totalCubes:
        tot += volume(cube)
    return tot
    
totalCubes = []
    
for i, line in enumerate(lines):
    if i == 20:
        print(getAns())
    line = line.strip()
    action, cubes = line.split()
    cubes = cubes.split(",")
    cuboid = []
    for cube in cubes:
        c = cube.split("=")
        c = c[1]
        c = [int(x) for x in c.split("..")]
        cuboid.append(c)
        
    x1 = cuboid[0][0]
    x2 = cuboid[0][1]
    y1 = cuboid[1][0]
    y2 = cuboid[1][1]
    z1 = cuboid[2][0]
    z2 = cuboid[2][1]
    c = Cuboid(x1, y1, z1, x2, y2, z2)
    if action == "on":
        addCubiod(c)
    else:
        removeCuboid(c)
        
print(getAns())