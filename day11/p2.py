
lines = []

with open('input.in') as f:
    lines = f.readlines()

octs = [[int(x) for x in line.strip()] for line in lines]
    
tot = 0
    
def flash(i, j):
    global octs
    global tot
    tot += 1
    octs[i][j] = 0
    ns = [(i, j-1), (i, j+1), (i-1, j), (i+1, j), (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]
    for ii, jj in ns:
        if 0 <= ii < len(octs) and 0 <= jj < len(octs[0]) and octs[ii][jj] != 0:
            octs[ii][jj] += 1
            if octs[ii][jj] > 9:
                flash(ii, jj)
    
for k in range(1000):
    allF = True
    for i in range(len(octs)):
        for j in range(len(octs[0])):
            if octs[i][j] != 0:
                allF = False
    
    if allF:
        print(k)
        break
    
    for i in range(len(octs)):
        for j in range(len(octs[0])):
            octs[i][j] += 1
    
    for i in range(len(octs)):
        for j in range(len(octs[0])):
            if octs[i][j] > 9:
                flash(i, j)
                