import re

lines = open(0).read().splitlines()

wins = []
for line in lines:
    lst = line.split(": ")[1]
    have, need = lst.split(" | ")
    have = set(map(int, re.findall(r'\d+', have)))
    need = set(map(int, re.findall(r'\d+', need)))

    score = len(have & need)
    wins.append(score)

copies = [1 for _ in range(len(lines))]

for i in range(len(lines)):
    for j in range(wins[i]):
        copies[i+j+1] += copies[i]

print(sum(map(lambda x: 2 ** (x - 1) if x > 0 else 0, wins)))
print(sum(copies))