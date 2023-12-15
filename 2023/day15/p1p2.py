from collections import defaultdict

parts = open(0).readline().split(",")

def hash(s):
    val = 0
    for c in s:
        val += ord(c)
        val *= 17
        val %= 256
    return val

buckets = defaultdict(list)
p1 = 0
for part in parts:
    p1 += hash(part)

    if "=" in part:
        p, num = part.split("=")
        bucket = hash(p)
        num = int(num)

        i = next((j for j, (pp, _) in enumerate(buckets[bucket]) if p == pp), None)

        if i is None:
            buckets[bucket].append((p, num))
        else:
            buckets[bucket][i] = (p, num)
    else:
        bucket = hash(part[:-1])
        i = next((j for j, (pp, _) in enumerate(buckets[bucket]) if part[:-1] == pp), None)

        if i is not None:
            buckets[bucket].pop(i)

p2 = 0
for bucket in buckets:
    for i, (_, num) in enumerate(buckets[bucket]):
        p2 += (bucket + 1) * (i + 1) * num

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")