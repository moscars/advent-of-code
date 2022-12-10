
lines = []

with open('input.in') as f:
    lines = f.readlines()
    
seq = lines[0]
lines.pop(0)
lines.pop(0)


lines = [line.strip() for line in lines]

changes = {}

for line in lines:
    comb, to = line.split(" -> ")
    changes[comb] = to
    

for _ in range(10):
    newseq = seq[0]
    for i in range(len(seq) - 1):
        f, s = seq[i], seq[i+1]
        comb = f + s
        if s == "\n": continue
        if comb in changes:
            newseq += changes[comb] + s
        else:
            newseq += s
    seq = newseq
    
count = {}
for char in seq:
    if char not in count:
        count[char] = 1
    else:
        count[char] += 1

ma = max([count[char] for char in seq])
mi = min([count[char] for char in seq])
print(ma - mi)
        
        
    
            
            
        