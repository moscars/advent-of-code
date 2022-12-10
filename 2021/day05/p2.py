
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
    while True:
        nums[y1][x1] += 1
        if x1 > x2:
            x1 -= 1
        elif x1 < x2:
            x1 += 1
        if y1 > y2:
            y1 -= 1
        elif y1 < y2:
            y1 += 1
        if x1 == x2 and y1 == y2:
            nums[y1][x1] += 1
            break
        
counter = 0
for row in nums:
    for elem in row:
        if elem >= 2:
            counter += 1

print(counter)