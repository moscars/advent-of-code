from z3 import *

lines = open(0).read().splitlines()

points = []
for line in lines:
    points.append(tuple(map(int, line.replace(" @", ",").split(","))))

s = Solver()

x = Int("x")
y = Int("y")
z = Int("z")

dx = Int("dx")
dy = Int("dy")
dz = Int("dz")

for i, point in enumerate(points):
    x1, y1, z1, dx1, dy1, dz1 = point

    t = Int(f"t_{i}")

    s.add(x + dx * t == x1 + dx1 * t)
    s.add(y + dy * t == y1 + dy1 * t)
    s.add(z + dz * t == z1 + dz1 * t)
    s.add(t >= 0)

assert s.check() == sat
m = s.model()

print(m[x].as_long() + m[y].as_long() + m[z].as_long())