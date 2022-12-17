
'''
Idea part 2: Find repeating states and then skip everything in between these repeating states

states are represented as (shapeOfFloor, current shape, and current location in the wind list)
When all of these are the same then everything will cycle until any multiple of this number of rocks
minus the number of rocks for the inital state.

These functions were used for finding where states repeat

localHeight = {}
states = {}
def getShapeOfFloor():
    assert (max(localHeight.values()) - min(localHeight.values())) <= 1
    top = []
    for x in range(7):
        top.append(localHeight[x])
    
    minTop = min(top)
    for i in range(len(top)):
        top[i] -= minTop
    
    return tuple(top)

def checkRepeating():
    state = (getShapeOfFloor(), shapeIndex, windIndex)

    if state not in states:
        states[state] = [highest, fallen, shapeIndex, windIndex]
    else:
        if fallen > 4_000_000:
            print(fallen)
            print(highest)
            print("Shape", states[state][2])
            print("Wind loc", states[state][3])
            print("Diff fallen", fallen - states[state][1])
            print("Diff height", highest - states[state][0])
            print(getShapeOfFloor())
            exit(0)
'''

line = open(0).read().splitlines()[0]

shapes = [
    [['#', '#', '#', '#']],

    [['.', '#', '.'], 
     ['#', '#', '#'],
     ['.', '#', '.']],

    [['.', '.', '#'],
     ['.', '.', '#'],
     ['#', '#', '#']],

    [['#'],
     ['#'],
     ['#'],
     ['#']],

    [['#', '#'],
    ['#', '#']],
]

def validHorizontalMove(shape, x, y, occupied):
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if shape[i][j] == '#' and ((x + j, y - i) in occupied or x + j < 0 or x + j >= 7):
                return False
    return True

def validVerticalMove(shape, x, y, occupied):
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if (y - i < 1) or (shape[i][j] == '#' and (x + j, y - i) in occupied):
                return False
    return True

def dropRocks(num, p2=False):
    occupied = set()
    fallen = 0
    windIndex = 0
    shapeIndex = 0
    highest = 0

    if p2:
        # inital state found
        startFall = 1821
        startHeight = 2876

        # repeats every ca 4 million rocks
        diffFall = 3998550
        # the height increases with this much each cycle
        diffHeight = 6337412

        # Cycle until we are almost at a trillion
        highest = startHeight
        fallen = startFall
        while fallen < 999996000000:
            fallen += diffFall
            highest += diffHeight

        # The repeating state I choose had
        # the following "floor" structure
        occupied.add((0, highest - 1))
        occupied.add((1, highest - 1))
        occupied.add((2, highest - 1))
        occupied.add((3, highest - 1))
        occupied.add((4, highest - 0))
        occupied.add((5, highest - 0))
        occupied.add((6, highest - 0))

        # The state had shape 1 and loc 435 in the wind
        shapeIndex = 1
        windIndex = 435


    while fallen < num:
        if p2 and (num - fallen) % 10_000 == 0:
            print("Rocks left:", num - fallen)
        shape = shapes[shapeIndex]
        fallen += 1
        shapeIndex += 1
        shapeIndex %= len(shapes)

        falling = True

        y = highest + len(shape) + 3
        x = 2
        while falling:
            wind = line[windIndex]
            windIndex += 1
            windIndex %= len(line)
            if wind == '>':
                x += 1
            else:
                x -= 1
            
            if not validHorizontalMove(shape, x, y, occupied):
                if wind == '>':
                    x -= 1
                else:
                    x += 1
            
            y -= 1
            if not validVerticalMove(shape, x, y, occupied):
                y += 1
                for i in range(len(shape)):
                    for j in range(len(shape[i])):
                        if shape[i][j] == '#':
                            highest = max(highest, y - i)
                            # This was used for finding the "floor" structure
                            # localHeight[j+x] = max(localHeight[j+x], y - i)
                            occupied.add((x + j, y - i))
                falling = False
    return highest
            
print(dropRocks(2022))
print(dropRocks(1_000_000_000_000, True))