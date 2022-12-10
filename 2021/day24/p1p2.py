import random
lines = []

with open('input.in') as f:
    lines = f.readlines()
    
for i in range(len(lines)):
    a = lines[i].split()
    if len(a) == 2:
        lines[i] = [a[0], a[1]]
    else:
        lines[i] = [a[0], (a[1], a[2])]
        
def monad(nums):
    index = 0
    variables = [0, 0, 0, 0]
    match = {"w": 0, "x": 1, "y": 2, "z": 3}
    for op, val in lines:  
        if op == "inp":
            variables[match[val]] = int(nums[index])
            index += 1
            continue
        v = variables[match[val[1]]] if val[1] in match else int(val[1])
        if op == "add":
            variables[match[val[0]]] += v
        elif op == "mul":
            variables[match[val[0]]] *= v
        elif op == "div":
            variables[match[val[0]]] //= v
        elif op == "mod":
            variables[match[val[0]]] %= v
        elif op == "eql":
            variables[match[val[0]]] = 1 if variables[match[val[0]]] == v else 0
                
    return variables[3]


def searchFromBestGuess(num, p2):
    best = 0
    cnt = 0
    lst = 0
    n = int(num)
    for i in range(n, 0 if p2 else 99999999999999, -1 if p2 else 1):
        s = str(i)
        if "0" in s:
            continue
        cnt += 1
        if cnt > lst + 1000000:
            break
        if monad(s) == 0:
            best = s
            lst = cnt
    return best


def getSomeAlmostAcceptedNumbers():
    good = set()
    for _ in range(4000000):
        n = random.randint(10000000000000, 99999999999999)
        s = str(n)
        if "0" in s:
            continue
        else:
            a = monad(s)
            if a < 2000:
                good.add(s)
    return good

def simulatedAnnealing(num):
    done = set()
    s = str(num)
    iterations = 0
    T = 2
    kmax = 100000
    iterations = 0
    k = 1
    prev = monad(s)
    while iterations < 700000:
        iterations += 1
        tk = k
        tmax = kmax
        T = 1 - (tk+1) / tmax
        if T < 0.001:
            T = 0.001
        n = random.randint(0, 13)
        r = random.randint(1, 9)
        f = s[:n] + str(r) + s[n+1:]
        a = monad(f)
        if a == 0:
            if f not in done:
                done.add(f)
        cost = a - prev
        if -1 * cost / T > 500:
            s = f
            k+=1
        else: 
            prob = pow(2.71828, -1 * cost / T)
            r = random.randint(0, 100000) / 100000
            if r < prob:
                s = f
                k+=1
    return done

#This is a Monte Carlo algorithm approach,
#more iterations in each function yields
#a higher probability of correct results 

print("Started searching for good starting points")
almostAccepted = getSomeAlmostAcceptedNumbers()
accepted = set()
print("Simulated annealing on", len(almostAccepted), "numbers")
for num in almostAccepted:
    foundAccepted = simulatedAnnealing(num)
    for num2 in foundAccepted:
        accepted.add(num2)
print(len(accepted), "accepted were found")
minSearch = min(accepted)
maxSearch = max(accepted)

print("Started final search")
print(searchFromBestGuess(maxSearch, False))
print(searchFromBestGuess(minSearch, True))
        