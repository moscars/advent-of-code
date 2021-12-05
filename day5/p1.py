
lines = []

with open('input.in') as f:
    lines = f.readlines()
    
    
nums = []
for i in range(1005):
    nums.append([0] * 1005)

for i in range(len(lines)):
    a = lines[i].split("->")
    first = a[0].split(",")
    second = a[1].split(",")
    x1 = int(first[0])
    y1 = int(first[1])
    x2 = int(second[0])
    y2 = int(second[1])
    if x1 > x2:
        tmp = x1
        x1 = x2
        x2 = tmp
    if y1 > y2:
        tmp = y1
        y1 = y2
        y2 = tmp
    if x1 == x2:
        for j in range(y1, y2+1):
            nums[j][x1] += 1
    if y1 == y2:
        for j in range(x1, x2+1):
            nums[y1][j] += 1
        
counter = 0
for row in nums:
    for elem in row:
        if elem >= 2:
            counter += 1

print(counter)