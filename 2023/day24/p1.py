from z3 import *

lines = open(0).read().splitlines()

points = []
for line in lines:
    points.append(tuple(map(int, line.replace(" @", ",").split(","))))

sm = 200000000000000
la = 400000000000000

tot = len(points) * (len(points) - 1) // 2
cnt = 0

ans = 0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        cnt += 1
        if cnt % 10 == 0:
            print(f"{cnt}/{tot}")

        p1 = points[i]
        p2 = points[j]

        x1, y1, _, dx1, dy1, _ = p1
        x2, y2, _, dx2, dy2, _ = p2

        s = Solver()

        t = Real("t")
        t2 = Real("t2")
        x = Real("x")
        y = Real("y")

        s.add(t >= 0)
        s.add(t2 >= 0)

        s.add(x == x1 + dx1 * t)
        s.add(y == y1 + dy1 * t)

        s.add(x == x2 + dx2 * t2)
        s.add(y == y2 + dy2 * t2)

        s.add(x >= sm)
        s.add(x <= la)

        s.add(y >= sm)
        s.add(y <= la)

        if s.check() == sat:
            ans += 1

print(ans)