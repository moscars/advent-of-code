import sys

data = sys.stdin.read()
elfs = data.splitlines()
p1, p2 = 0, 0

def score(c):
    if c.isupper():
        return ord(c) - ord('A') + 27
    else:
        return ord(c) - ord('a') + 1

for elf in elfs:
    firstHalf, secondHalf = set(elf[:len(elf)//2]), set(elf[len(elf)//2:])

    for c in firstHalf:
        if c in secondHalf:
            p1 += score(c)

for i in range(2, len(elfs), 3):
    first, second, third = set(elfs[i]), set(elfs[i-1]), set(elfs[i-2])

    for c in first:
        if c in second and c in third:
            p2 += score(c)

print(p1)
print(p2)