
lines = open(0).read().splitlines()

class Monkey:
    def __init__(self):
        self.num = None
        self.first = None
        self.op = None
        self.second = None

monkeys = {}
for line in lines:
    m = Monkey()
    name, rest = line.split(':')
    monkeys[name] = m

    expr = rest.split()
    if len(expr) == 1:
        m.num = int(expr[0])
        continue
    
    m.first, m.op, m.second = expr[0], expr[1], expr[2]

def solve(name):
    curr = monkeys[name]
    if name == "root":
        first, second = solve(curr.first), solve(curr.second)
        return first, second, eval(f"{first} {curr.op} {second}")

    if curr.num is not None:
        return curr.num
    
    return eval(f"{solve(curr.first)} {curr.op} {solve(curr.second)}")

def binarySearch(compare):
    lo, hi = 0, int(1e16)
    while lo <= hi:
        mid = (lo + hi) // 2
        monkeys["humn"].num = mid
        first, second, _ = solve("root")
        if first == second:
            return mid
        if compare(first, second):
            lo = mid + 1
        else:
            hi = mid - 1
    return 0

print(int(solve("root")[2]))
print(binarySearch(lambda x, y: x < y) | binarySearch(lambda x, y: x > y))