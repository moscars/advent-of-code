import sys
from copy import deepcopy

stackData, lines = [x.splitlines() for x in sys.stdin.read().split('\n\n')]

stacks = [[] for _ in range(9)]
for line in stackData:
    i = 1
    for index in range(9):
        if line[i] != ' ':
            stacks[index].append(line[i])
        i += 4

for i in range(len(stacks)):
    stacks[i] = stacks[i][::-1]

stacks1 = deepcopy(stacks)
stacks2 = deepcopy(stacks)

for line in lines:
    mv = line.split()
    amt, prev, to = int(mv[1]), int(mv[3]) - 1, int(mv[5]) - 1

    for (stacks, p2) in [(stacks1, False), (stacks2, True)]:
        move = stacks[prev][-amt:]

        stacks[to] += move if p2 else move[::-1]
        stacks[prev] = stacks[prev][:-amt]

print(''.join([s[-1] for s in stacks1]))
print(''.join([s[-1] for s in stacks2]))