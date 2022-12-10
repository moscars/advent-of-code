
lines = []

with open('input.txt') as f:
    lines = f.readlines()

hor = 0
depth = 0
aim = 0
for line in lines:
    l = line.split()
    move = l[0]
    amount = int(l[1])
    if move == "down":
        aim += amount
    elif move == "up":
        aim -= amount
    elif move == "forward":
        hor += amount
        depth += aim * amount

print(hor * depth)