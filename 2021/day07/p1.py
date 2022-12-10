
lines = []

with open('input.in') as f:
    lines = f.readlines()

pos = lines[0].split(",")
for i in range(len(pos)):
    pos[i] = int(pos[i])
    
pos.sort()


mid = pos[len(pos) // 2]

diff = 0
for p in pos:
    diff += abs(p - mid)
    
    
print(diff)
