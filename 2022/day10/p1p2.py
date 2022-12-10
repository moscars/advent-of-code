
lines = open(0).read().splitlines()

actions = []
for line in lines:
    if line == "noop":
        actions.append(0)
        continue
    actions.append(0)
    actions.append(int(line.split()[1]))

pic, row = [], []
x, i, p1 = 1, 1, 0
for add in actions:
    if (i - 20) % 40 == 0:
        p1 += x * i
    
    if len(row) in range(x - 1, x + 2):
        row.append("#")
    else:
        row.append(" ")
    
    if i % 40 == 0:
        pic.append(row)
        row = []

    x += add
    i += 1

print(p1)
for row in pic:
    print(" ".join(row))