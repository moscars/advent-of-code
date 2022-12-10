
p1, p2 = 0, 0
for line in open(0):
    for i in range(len(line)):
        s1 = set(line[i-3:i+1])
        s2 = set(line[i-13:i+1])
        if len(s1) == 4 and p1 == 0:
            p1 = i + 1
        if len(s2) == 14 and p2 == 0:
            p2 = i + 1

print(p1)
print(p2)