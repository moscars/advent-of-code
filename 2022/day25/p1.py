lines = open(0).read().splitlines()

value = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}

def convert(char, power):
    return value[char] * (5 ** power)

target = 0
for line in lines:
    for p, char in enumerate(line[::-1]):
        target += convert(char, p)

number = []
curr = 0
def backtrack(power):
    global curr
    
    if power == -1 and curr == target:
        print(''.join(number))
        exit(0)
    
    if power == -1:
        return

    maxReachableBound = curr + convert('2', power + 1)
    minReachableBound = curr + convert('=', power + 1)
    if maxReachableBound < target or minReachableBound > target:
        return
    
    for nxt in value.keys():
        number.append(nxt)
        curr += convert(nxt, power)
        backtrack(power - 1)
        curr -= convert(nxt, power)
        number.pop()

depth = 0
while True:
    depth += 1
    backtrack(depth)