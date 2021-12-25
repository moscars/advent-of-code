from queue import PriorityQueue

lines = []

with open('input.in') as f:
    lines = f.readlines()

mapp1 = [["0" for _ in range(len(lines[0]))] for _ in range(len(lines))]
for i in range(len(lines)):
    for j in range(len(lines[i])):
        mapp1[i][j] = lines[i][j]
  
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if mapp1[i][j] not in ["A", "B", "C", "D", "#", "."]:
            mapp1[i][j] = "#"
        if mapp1[i][j] == ".":
            mapp1[i][j] = " "

for i in range(6):
    r = []
    for j in range(len(lines[0])):
        r.append("#")
    mapp1.append(r)
    
costt = {
    "A": 1,
    "B": 10,
    "C": 100,
    "D": 1000
}

spot = {
    "A": 3,
    "B": 5,
    "C": 7,
    "D": 9
}

def getDoneFromStart():
    doneFromStart = []
    for j in range(3, 10, 2):
        last = "#"
        for i in range(6, 1, -1):
            if mapp1[i][j] != "#" and last == "#" and j == spot[mapp1[i][j]]:
                doneFromStart.append([i, j])
            last = mapp1[i][j]
    return doneFromStart
    
def isDone(m):
    for i in range(3, 10, 2):
        row = [m[5][i], m[4][i], m[3][i], m[2][i]]
        if m[2][i] == " ":
            return False
        for g in row:
            if g not in [m[2][i], "#"]:
                return False
    return True

def makeHashable(mapp, hasToMove):
    s = []
    for row in mapp:
        for elem in row:
            s.append(elem)
    s.append(",")
    s.append(str(hasToMove[0]))
    s.append(",")
    s.append(str(hasToMove[1]))
    return ''.join(s)

def scoreMap(m, p2):
    sc = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] in spot:
                kind = m[i][j]
                add = abs(j - spot[kind]) * costt[kind]
                sc += add
                if add > 0:
                    sc += (abs(i - 1) * costt[kind])
                    sc += costt[kind]
                    if p2: sc += costt[kind]
                else:
                    for ii in range(i+1, 6):
                        if m[ii][j] not in [kind, "#", " "]:
                            sc += 2 * (abs(i - 1) * costt[kind])
                            sc += 3 * costt[kind]
                            break
    return sc

def move(i, j, newi, newj, mapp, done, hasToMove, up):
    m = [[x for x in row] for row in mapp]
    d = [[y for y in row] for row in done]
    m[newi][newj] = m[i][j]
    m[i][j] = " "
    if (up and newi != 1) or (not up and hasToMove is not None):
        return [m, [newi, newj], [newi, newj], d]
    else:
        return [m, [newi, newj], None, d]

def moveToAllPossible(mapp, i, j, hasToMove, done):
    out = []
    kind = mapp[i][j]
    
    hasMovedDown = False
    if mapp[i+1][j] == " " and j == spot[kind] and mapp[i+2][j] in [kind, "#"] and mapp[i+3][j] in [kind, "#"] and mapp[i+4][j] in [kind, "#"]:
        out.append(move(i, j, i+1, j, mapp, done, None, False))
        #this amphipod is done
        out[-1][3].append([i+1, j])
        hasMovedDown = True
    
    down = [mapp[i+1][j], mapp[i+2][j], mapp[i+3][j], mapp[i+4][j], mapp[i+5][j]]
    mv = False
    for k in spot:
        if k != kind:
            if k in down:
                mv = True
                
    if not mv and mapp[i+1][j] == " " and j == spot[kind] and mapp[i+2][j] == " ":
        out.append(move(i, j, i+1, j, mapp, done, hasToMove, False))
        hasMovedDown = True
    if not hasMovedDown and mapp[i-1][j] == " ":
        out.append(move(i, j, i-1, j, mapp, done, hasToMove, True))
    if not hasMovedDown and mapp[i][j+1] == " ":
        out.append(move(i, j, i, j+1, mapp, done, hasToMove, False))
    if not hasMovedDown and mapp[i][j-1] == " ":
        out.append(move(i, j, i, j-1, mapp, done, hasToMove, False))
    
    return out

def getPossibleNeighbourStates(mapp, lastMoved, hasToMove, done):
    neighs = []
    
    #move anyone that has to move
    if hasToMove is not None:
        i = hasToMove[0]
        j = hasToMove[1]
        possibleMoves = moveToAllPossible(mapp, i, j, hasToMove, done)
        for m in possibleMoves:
            neighs.append(m)
        return neighs
    
    #check if someone has to move out of the way
    someoneHasToMove = False
    for j in range(3, 10, 2):
        if mapp[1][j] != " ":
            someoneHasToMove = True
            possibleMoves = moveToAllPossible(mapp, 1, j, None, done)
            for m in possibleMoves:
                neighs.append(m)
    if someoneHasToMove:
        return neighs

    #move everyone that can move
    for i in range(len(mapp)):
        if i > 5: break
        for j in range(len(mapp[0])):
            if mapp[i][j] in ["A", "B", "C", "D"] and [i, j] not in done:
                possibleMoves = []
                if i == 1 and (lastMoved[0] != i or lastMoved[1] != j):
                    possibleMoves = moveToAllPossible(mapp, i, j, [i, j], done)
                else:
                    possibleMoves = moveToAllPossible(mapp, i, j, None, done)
                for mv in possibleMoves:
                    neighs.append(mv)
    return neighs

def astar(p2=False):
    if p2:
        tmp = mapp1[3]
        mapp1[3] = ["#", "#", "#", "D", "#", "C", "#", "B", "#", "A", "#", "#", "#", "#"]
        mapp1[4] = ["#", "#", "#", "D", "#", "B", "#", "A", "#", "C", "#", "#", "#", "#"]
        mapp1[5] = tmp
    
    done = getDoneFromStart()
    
    seen = set()
    q = PriorityQueue()
    q.put((0, 0, mapp1, [0, 0], [-1, -1], done))
    while not q.empty():
        tcost, cost, mapp, lastMoved, hasToMove, done = q.get()
                
        if isDone(mapp):
            return cost
        
        if makeHashable(mapp, hasToMove) in seen:
            continue
        seen.add(makeHashable(mapp, hasToMove))
        
        for neigh in getPossibleNeighbourStates(mapp, lastMoved, hasToMove if hasToMove != [-1, -1] else None, done):
            m = neigh[0]
            last = neigh[1]
            has = neigh[2]
            doneList = neigh[3]
            c = cost + costt[m[last[0]][last[1]]]
            estimateLeft = scoreMap(m, p2)
            q.put((c + estimateLeft, c, m, last, has if has is not None else [-1, -1], doneList))

print(astar())
print(astar(True))

