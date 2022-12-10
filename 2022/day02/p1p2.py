import sys

data = sys.stdin.read()
lines = data.splitlines()

vals = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

scores = [0, 3, 6]
def wePlayOur(op, our):
    idx = ord(our) - ord('X')
    if op == 'A':
        return scores[(idx + 1) % 3]
    elif op == 'B':
        return scores[idx]
    elif op == 'C':
        return scores[(idx - 1) % 3]

moves = ['X', 'Y', 'Z']
def wePlayGivenOutcome(op, outcome):
    idx = ord(outcome) - ord('X')
    if op == 'A':
        return moves[(idx - 1) % 3]
    elif op == 'B':
        return moves[idx]
    elif op == 'C':
        return moves[(idx + 1) % 3]

p1, p2 = 0, 0
for line in lines:
    op, our = line.split()

    p1 += vals[our]
    p1 += wePlayOur(op, our)

    p2 += vals[wePlayGivenOutcome(op, our)]
    p2 += wePlayOur(op, wePlayGivenOutcome(op, our))

print(p1)
print(p2)