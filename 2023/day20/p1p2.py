from collections import defaultdict
from collections import deque
import math

lines = open(0).read().splitlines()

class Module:
    def __init__(self):
        pass

    def process(self, _, inp):
        return inp

class FlipFlop(Module):
    def __init__(self):
        self.state = 0

    def process(self, _, inp):
        if inp == 0:
            self.state = 0 if self.state == 1 else 1
            return self.state
        else:
            return None

class Conjuction(Module):
    def __init__(self):
        self.mem = defaultdict(int)

    def process(self, name, inp):
        self.mem[name] = inp
        if all(val == 1 for val in self.mem.values()):
            return 0
        return 1 
    
neighs = defaultdict(list)
incoming = defaultdict(list)
mods = {}

for line in lines:
    name, rest = line.split(" -> ")
    rest = rest.split(", ")
    if name != "broadcaster":
        t = name[0]
        name = name[1:]
    else:
        t = None
    
    neighs[name] = rest
    for n in rest:
        incoming[n].append(name)

    if t == "%":
        mods[name] = FlipFlop()
    elif t == "&":
        mods[name] = Conjuction()
    else:
        mods[name] = Module()

for mod in mods:
    if type(mods[mod]) == Conjuction:
        mods[mod].mem = {n:0 for n in incoming[mod]}

assert len(incoming["rx"]) == 1
inputRx = incoming["rx"][0]
cycles = defaultdict(list)

totLow = totHigh = i = 0
while len(cycles) < 4 or any(len(samples) < 2 for samples in cycles.values()):
    i += 1
    q = deque()
    q.append(("broadcaster", "prev", 0))
    while q:
        name, prev, inp = q.popleft()

        if i < 1000:
            totLow += 1 if inp == 0 else 0
            totHigh += 1 if inp == 1 else 0

        if name == "rx":
            continue

        res = mods[name].process(prev, inp)
        if res is not None:
            for neigh in neighs[name]:
                q.append((neigh, name, res))
        
        if name == inputRx:
            for inp in mods[name].mem:
                if mods[name].mem[inp] == 1 and i not in cycles[inp]:
                    cycles[inp].append(i)

cycleLengths = []
for inp in cycles:
    cycleLengths.append(cycles[inp][1] - cycles[inp][0])

print(f"Part 1: {totLow * totHigh}")
print(f"Part 2: {math.lcm(*cycleLengths)}")