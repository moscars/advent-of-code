import functools

groups = open(0).read().split('\n\n')

def comp(l1, l2):
    if isinstance(l1, int) and isinstance(l2, int):
        if l1 < l2:
            return -1
        if l1 == l2:
            return 0
        return 1
    
    if isinstance(l1, int) and isinstance(l2, list):
        return comp([l1], l2)
    if isinstance(l1, list) and isinstance(l2, int):
        return comp(l1, [l2])

    for i in range(min(len(l1), len(l2))):
        val = comp(l1[i], l2[i])
        if val != 0:
            return val

    return comp(len(l1), len(l2))

p1 = 0
packets = []

packets.append([[2]])
packets.append([[6]])
for i, group in enumerate(groups):
    l1, l2 = map(eval, group.split('\n'))
    if comp(l1, l2) == -1:
        p1 += i + 1
    packets.append(l1)
    packets.append(l2)

packets = sorted(packets, key=functools.cmp_to_key(comp))

p2 = 1
for i in range(len(packets)):
    if packets[i] in [[[2]], [[6]]]:
        p2 *= (i + 1)
print(p1)
print(p2)