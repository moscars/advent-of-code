from collections import deque, defaultdict

g = [list(line) for line in open(0).read().splitlines()]
R, C = len(g), len(g[0])

def calcNumInCopy(gI, gJ, ansSet):
    cnt = 0
    for i in range(R * gI, R * gI + R):
        for j in range(C * gJ, C * gJ + C):
            if (i, j) in ansSet:
                cnt += 1
    return cnt

def simulate(si, sj, maxDepth):
    q = deque()
    q.append((si, sj, 0))
    seen = set()
    ansSet = set()
    while q:
        i, j, d = q.popleft()
        if (i, j, d) in seen:
            continue
        seen.add((i, j, d))
        if d == maxDepth:
            ansSet.add((i, j))
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj

            virtualNi, virtualNj = ni % R, nj % C

            if g[virtualNi][virtualNj] != "#" and d + 1 <= maxDepth:
                q.append((ni, nj, d + 1))

    return ansSet

si, sj = next((i, j) for i in range(R) for j in range(C) if g[i][j] == "S")
print(f"Part 1: {len(simulate(si, sj, 64))}")


halfR = R // 2
assert R == C
assert R % 2 == 1
assert si == sj == halfR
assert (26501365 - halfR) % R == 0

n = (26501365 - halfR) // R

ansSet = simulate(si, sj, 2 * R + halfR)

b = 8
cnt = defaultdict(int)
for i in range(-b, b):
    for j in range(-b, b):
        v = calcNumInCopy(i, j, ansSet)
        cnt[(i, j)] = v

ans = 0
# corners
ans += 1 * cnt[(-2, 0)]
ans += 1 * cnt[(2, 0)]
ans += 1 * cnt[(0, -2)]
ans += 1 * cnt[(0, 2)]
# outer edges
ans += n * cnt[(-2, -1)]
ans += n * cnt[(-2, 1)]
ans += n * cnt[(2, -1)]
ans += n * cnt[(2, 1)]
# inner edges
ans += (n - 1) * cnt[(-1, -1)]
ans += (n - 1) * cnt[(-1, 1)]
ans += (n - 1) * cnt[(1, -1)]
ans += (n - 1) * cnt[(1, 1)]
# inner 1
ans += n ** 2 * cnt[(-1, 0)]
# inner 2
ans += (n - 1) ** 2 * cnt[(0, 0)]


print(f"Part 2: {ans}")