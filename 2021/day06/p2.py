
lines = []

with open('input.in') as f:
    lines = f.readlines()

fish = lines[0].split(",")

for i in range(len(fish)):
    fish[i] = int(fish[i])
    
fishAt = []

for i in range(10):
    counter = 0
    for f in fish:
        if f == i:
            counter += 1
    fishAt.append(counter)
            

new = 0
neww = 0
for i in range(256):
    for j in range(len(fishAt) - 1):
        fishAt[j] = fishAt[j+1]
    new = fishAt[0]
    
    fishAt[8] += neww
    fishAt[7] += new
    fishAt[0] = 0
    neww = new
        

print(sum(fishAt))