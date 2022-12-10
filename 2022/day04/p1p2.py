import sys

lines = sys.stdin.read().splitlines()

def fullyContains(f1, f2, s1, s2):
    return f1 <= s1 and s2 <= f2 or s1 <= f1 and f2 <= s2

def overlaps(f1, f2, s1, s2):
    return s1 <= f1 <= s2 or s1 <= f2 <= s2 or fullyContains(f1, f2, s1, s2)

p1, p2 = 0, 0
for line in lines:
    range1, range2 = line.split(",")

    f1, f2 = map(int, range1.split("-"))
    s1, s2 = map(int, range2.split("-"))

    if fullyContains(f1, f2, s1, s2):
        p1 += 1
    if overlaps(f1, f2, s1, s2):
        p2 += 1

print(p1)
print(p2)