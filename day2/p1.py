
lines = []

with open('input.txt') as f:
    lines = f.readlines()

hor = 0
depth = 0
for line in lines:
    l = line.split()
    move = l[0]
    amount = int(l[1])
    if move == "down":
        depth += amount
    elif move == "up":
        depth -= amount
    elif move == "forward":
        hor += amount

print(hor * depth)