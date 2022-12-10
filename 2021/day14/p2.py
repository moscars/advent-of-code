lines = []

with open('input.in') as f:
    lines = f.readlines()
    
seq = lines[0].strip()
lines.pop(0)
lines.pop(0)

seen = set()

lines = [line.strip() for line in lines]

changes = {}
count = {}

for line in lines:
    comb, to = line.split(" -> ")
    changes[comb] = to
    seen.add(to)
    seen.add(comb[0])
    seen.add(comb[1])
                
alreadyEval = {}

def evaluate(f, s, depth):
    ret = {}
    if depth == 0:
        for char in seen:
            ret[char] = 0
        for char in [f, s]:
            ret[char] += 1
        return ret
    
    comb = f + s
    if comb in changes:
        val = changes[comb]
        
        v1 = {}
        v2 = {}
        s1 = (f, val, depth - 1)
        s2 = (val, s, depth - 1)

        if s1 in alreadyEval:
            v1 = alreadyEval[s1]
        else:
            v1 = evaluate(f, val, depth - 1)
            alreadyEval[s1] = v1
        
        if s2 in alreadyEval:
            v2 = alreadyEval[s2]
        else:
            v2 = evaluate(val, s, depth - 1)
            alreadyEval[s2] = v2
            
        ret = {}
        for char in v1:
            if char not in ret:
                ret[char] = 0
            ret[char] += v1[char]
        for char in v2:
            if char not in ret:
                ret[char] = 0
            ret[char] += v2[char]
        ret[val] -= 1
    return ret

seq = [char for char in seq if char != "\n"]
                   
for i in range(len(seq) - 1):
    f, s = seq[i], seq[i+1]
    v1 = evaluate(f, s, 40)
    for char in v1:
        if char not in count:
            count[char] = 0
        count[char] += v1[char]
    if i != len(seq) - 2:
        count[s] -= 1
            
ma = max([count[char] for char in seen])
mi = min([count[char] for char in seen])
print(ma - mi)
        
        
    
            
            
        