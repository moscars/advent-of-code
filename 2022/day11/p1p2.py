from copy import deepcopy

monkeyLines = open(0).read().split('\n\n')

class Monkey():
    def __init__(self, items, div, func, iftrue, iffalse):
        self.items = items
        self.div = div
        self.func = func
        self.iftrue = iftrue
        self.iffalse = iffalse
        self.seen = 0

monkeys = {}

def factory(op, val):
    if val == "old":
        return lambda x: x * x
    elif op == '*':
        return lambda x: x * int(val)
    else:
        return lambda x: x + int(val)

for i, monk in enumerate(monkeyLines):
    lines = monk.splitlines()
    op, val = lines[2].split('old ')[1].split()
    f = factory(op, val)

    items = [int(x) for x in lines[1][18:].split(',')]
    
    div = int(lines[3].split()[-1])
    iftrue = int(lines[4].split()[-1])
    iffalse = int(lines[5].split()[-1])
    monkeys[i] = Monkey(items, div, f, iftrue, iffalse)

primeProd = 1
for monkey in monkeys.values():
    primeProd *= monkey.div

monkeysp2 = deepcopy(monkeys)

for rounds, monkeys in [(20, monkeys), (10000, monkeysp2)]:
    for r in range(rounds):
        for i in range(len(monkeys)):
            for item in monkeys[i].items:
                monkeys[i].seen += 1
                item = monkeys[i].func(item)
                if rounds == 20: 
                    item //= 3
                else: 
                    item %= primeProd
                
                if item % monkeys[i].div == 0:
                    monkeys[monkeys[i].iftrue].items.append(item)
                else:
                    monkeys[monkeys[i].iffalse].items.append(item)
            monkeys[i].items = []
        
    seen = sorted([monkey.seen for monkey in monkeys.values()])
    print(seen[-1] * seen[-2])