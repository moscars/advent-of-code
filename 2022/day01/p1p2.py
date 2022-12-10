import sys

data = sys.stdin.read()
lines = data.split('\n\n')

calories = []
for line in lines:
    vals = line.split()
    calories.append(sum(list(map(int, vals))))

calories.sort()

print(calories[-1])
print(calories[-1] + calories[-2] + calories[-3])