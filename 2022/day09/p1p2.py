
lines = open(0).read().splitlines()

knots = [[0, 0] for _ in range(10)]
s1, s2 = {(0, 0)}, {(0, 0)}

move = {
    'R': lambda x: [x[0], x[1] + 1],
    'L': lambda x: [x[0], x[1] - 1],
    'U': lambda x: [x[0] - 1, x[1]],
    'D': lambda x: [x[0] + 1, x[1]],
}

for line in lines:
    direction, dist = line.split()
    for _ in range(int(dist)):
        knots[0] = move[direction](knots[0])
        
        for k in range(1, len(knots)):
            pi, pj = knots[k - 1]
            i, j = knots[k]
            di = abs(pi - i)
            dj = abs(pj - j)

            if di <= 1 and dj <= 1:
                continue
            
            if pi > i:
                i += 1
            elif pi < i:
                i -= 1
            if pj > j:
                j += 1
            elif pj < j:
                j -= 1

            if k == 1: s1.add((i, j))
            if k == 9: s2.add((i, j))
            knots[k] = [i, j]

print(len(s1))
print(len(s2))