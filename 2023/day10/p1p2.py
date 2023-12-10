from collections import defaultdict, deque

lines = open(0).read().splitlines()
g = [list(line) for line in lines]

R, C = len(g), len(g[0])

si, sj = 0, 0
for i in range(R):
    for j in range(C):
        if g[i][j] == "S":
            si, sj = i, j
            break

mp = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, -1), (0, 1)],
    "L": [(-1, 0), (0, 1)],
    "7": [(1, 0), (0, -1)],
    "J": [(-1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
}

p1 = 0
for choice in ["-", "|", "L", "7", "J", "F"]:
    g[si][sj] = choice
    q = deque([(si, sj, 0, -1, -1)])
    dists = [[float("inf") for _ in range(C)] for _ in range(R)]
    prev = defaultdict(list)

    ma = 0
    while len(q) > 0:
        i, j, d, pi, pj = q.popleft()
        prev[(i, j)].append((pi, pj))

        if dists[i][j] <= d:
            continue
        dists[i][j] = d
        ma = max(ma, d)

        for ii, jj in mp[g[i][j]]:
            ii += i
            jj += j
            if 0 <= ii < R and 0 <= jj < C and g[ii][jj] != ".":
                q.append((ii, jj, d + 1, i, j))

    cnt = 0
    for val in prev:
        if len(prev[val]) != 2:
            cnt += 1

    if cnt == 1 and ma != 0:
        p1 = ma
        break

largeGrid = [['.' for _ in range(C * 3)] for _ in range(R * 3)]
blocked = set()
for i in range(R):
    for j in range(C):
        if (i, j) in prev:
            for ii in range(3):
                for jj in range(3):
                    blocked.add((i * 3 + ii, j * 3 + jj))
            if g[i][j] == "L":
                largeGrid[i * 3 + 0][j * 3 + 1] = "#"
                largeGrid[i * 3 + 1][j * 3 + 1] = "#"
                largeGrid[i * 3 + 1][j * 3 + 2] = "#"
            elif g[i][j] == "7":
                largeGrid[i * 3 + 1][j * 3 + 0] = "#"
                largeGrid[i * 3 + 1][j * 3 + 1] = "#"
                largeGrid[i * 3 + 2][j * 3 + 1] = "#"
            elif g[i][j] == "J":
                largeGrid[i * 3 + 0][j * 3 + 1] = "#"
                largeGrid[i * 3 + 1][j * 3 + 1] = "#"
                largeGrid[i * 3 + 1][j * 3 + 0] = "#"
            elif g[i][j] == "F":
                largeGrid[i * 3 + 1][j * 3 + 1] = "#"
                largeGrid[i * 3 + 1][j * 3 + 2] = "#"
                largeGrid[i * 3 + 2][j * 3 + 1] = "#"
            elif g[i][j] == "-":
                largeGrid[i * 3 + 1][j * 3 + 0] = "#"
                largeGrid[i * 3 + 1][j * 3 + 1] = "#"
                largeGrid[i * 3 + 1][j * 3 + 2] = "#"
            elif g[i][j] == "|":
                largeGrid[i * 3 + 0][j * 3 + 1] = "#"
                largeGrid[i * 3 + 1][j * 3 + 1] = "#"
                largeGrid[i * 3 + 2][j * 3 + 1] = "#"

q = deque([(0, 0)])
outside = set()
while len(q) > 0:
    i, j = q.popleft()
    if (i, j) in outside:
        continue
    outside.add((i, j))

    for ii, jj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        if 0 <= ii < R * 3 and 0 <= jj < C * 3 and largeGrid[ii][jj] != "#":
            q.append((ii, jj))

p2 = 0
for i in range(R * 3):
    for j in range(C * 3):
        if not (i, j) in blocked and not (i, j) in outside:
            p2 += 1

p2 //= 9

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")