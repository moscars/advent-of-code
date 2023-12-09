
lines = open(0).read().splitlines()

p1, p2 = 0, 0
for line in lines:
    line = list(map(int, line.split()))

    rounds = []
    while not all(d == 0 for d in line):
        rounds.append(line)
        line = [line[i+1] - line[i] for i in range(len(line) - 1)]
    
    first, last = 0, 0
    for r in rounds[::-1]:
        first = r[0] - first
        last = r[-1] + last
    
    p1 += last
    p2 += first

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")