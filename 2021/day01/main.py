
lines = []

with open('input.txt') as f:
    lines = f.readlines()

prev = float("inf")

sums = []
for i in range(len(lines) - 2):
    sums.append(0)
    for j in range(i, i+3):
        sums[i] += int(lines[j])

prev = float("inf")
tot = 0
for s in sums:
    if s > prev:
        tot += 1
    prev = s
    
print(tot)