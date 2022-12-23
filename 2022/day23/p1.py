from collections import defaultdict
lines = open(0).read().splitlines()

grid = set([(i, j) for i, line in enumerate(lines) for j, c in enumerate(line) if c == '#'])
dirs = ['N', 'S', 'W', 'E']
locs = {
    'N': [lambda i, j: (i-1, j), lambda i, j: (i-1, j+1), lambda i, j: (i-1, j-1)],
    'S': [lambda i, j: (i+1, j), lambda i, j: (i+1, j+1), lambda i, j: (i+1, j-1)],
    'W': [lambda i, j: (i, j-1), lambda i, j: (i+1, j-1), lambda i, j: (i-1, j-1)],
    'E': [lambda i, j: (i, j+1), lambda i, j: (i+1, j+1), lambda i, j: (i-1, j+1)]
}

def getBox(grid):
    miJ = min([j for _, j in grid])
    maJ = max([j for _, j in grid])
    miI = min([i for i, _ in grid])
    maI = max([i for i, _ in grid])
    return (maI - miI + 1) * (maJ - miJ + 1) - len(grid)

proposed = {}
cnt = defaultdict(int)
movement = True
iterations = 0
while movement:
    movement = False
    iterations += 1
    for i, j in grid:
        if all([loc(i, j) not in grid for dirr in dirs for loc in locs[dirr]]):
            continue
        for dirr in dirs:
            if any([loc(i, j) in grid for loc in locs[dirr]]):
                continue
            proposed[(i, j)] = locs[dirr][0](i, j)
            cnt[proposed[(i, j)]] += 1
            break

    tmp = set()
    for i, j in grid:
        if (i, j) not in proposed or cnt[proposed[(i, j)]] > 1:
            tmp.add((i, j))
        else:
            movement = True
            tmp.add(proposed[(i, j)])
    
    grid = tmp
    dirs.append(dirs.pop(0))
    cnt.clear()
    proposed.clear()
    
    if iterations == 10:
        print(getBox(grid))
    
    if not movement:
        print(iterations)
