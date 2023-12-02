from collections import defaultdict

lines = open(0).read().splitlines()

p1, p2 = 0, 0
for i, line in enumerate(lines):
    line = line.split()[2:]
    vals = defaultdict(int)
    for j in range(0, len(line), 2):
        color = line[j+1].strip(",;")
        vals[color] = max(int(line[j]), vals[color])

    if vals["red"] <= 12 and vals["green"] <= 13 and vals["blue"] <= 14:
        p1 += i + 1

    p2 += vals["red"] * vals["green"] * vals["blue"]

print(p1)
print(p2)