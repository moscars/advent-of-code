import math
lines = []

with open('input.in') as f:
    lines = f.readlines()

pos = lines[0].split(",")
for i in range(len(pos)):
    pos[i] = int(pos[i])
    
pos.sort()

def calcTotCost(pos, cost):
    val = 0
    for p in pos:
        for v in range(abs(p - cost) + 1):
            val += v
    return val

ave = 0
for p in pos:
    ave += p

ave //= len(pos)
print(ave)
print(calcTotCost(pos, ave))