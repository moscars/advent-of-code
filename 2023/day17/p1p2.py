from collections import defaultdict
from queue import PriorityQueue

lines = open(0).read().splitlines()

g = [[int(c) for c in line] for line in lines]
R, C = len(g), len(g[0])

def opposite(di1, dj1, di2, dj2):
    if di1 == -di2 and dj1 == -dj2: return True
    return False

for (part, lowerBound, upperBound) in [(1, 0, 3), (2, 4, 10)]:
    q = PriorityQueue()
    cost = defaultdict(lambda: float("inf"))
    # cost, i, j, di, dj, numSteps
    q.put((0, 0, 0, 0, 1, 0))
    q.put((0, 0, 0, 1, 0, 0))

    ans = float("inf")
    cc = 0
    while not q.empty():
        c, i, j, di, dj, numSteps = q.get()
        neighs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        if i == R - 1 and j == C - 1 and numSteps >= lowerBound:
            ans = min(ans, c)
            continue

        for ii, jj in neighs:
            if opposite(di, dj, ii, jj): continue
            ni = i + ii
            nj = j + jj

            if 0 <= ni < R and 0 <= nj < C:
                newC = c + g[ni][nj]
                if ii == di and jj == dj:
                    if numSteps + 1 <= upperBound:
                        if newC < cost[(ni, nj, ii, jj, numSteps + 1)]:
                            cost[(ni, nj, ii, jj, numSteps + 1)] = newC
                            q.put((newC, ni, nj, ii, jj, numSteps + 1))
                else:
                    if numSteps >= lowerBound:
                        if newC < cost[(ni, nj, ii, jj, 1)]:
                            cost[(ni, nj, ii, jj, 1)] = newC
                            q.put((newC, ni, nj, ii, jj, 1))

    print(f"Part {part}: {ans}")