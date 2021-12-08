
lines = []

with open('input.in') as f:
    lines = f.readlines()

numsAfter = []
for i in range(len(lines)):
    l = lines[i].split("|")
    ll = l[1]
    ll = ll.split()
    for a in ll:
        numsAfter.append(a)

#print(len(numsAfter))

cnt = 0
for dig in numsAfter:
    if len(dig) == 7 or len(dig) == 3 or len(dig) == 4 or len(dig) == 2:
        cnt += 1

print(cnt)