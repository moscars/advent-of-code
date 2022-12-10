
lines = []

with open('input.in') as f:
    lines = f.readlines()

fish = lines[0].split(",")

for i in range(len(fish)):
    fish[i] = int(fish[i])
    
    
new = 0
neww = 0
for i in range(80):
    new = 0
    for j in range(len(fish)):
        fish[j] -= 1
        if fish[j] == 0:
            new += 1
            fish[j] = 7
    for j in range(neww):
        fish.append(8)
    neww = new

print(len(fish))