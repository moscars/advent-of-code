
lines = []

with open('input.in') as f:
    lines = f.readlines()


def onlyNums(nums, strip):
    for i in range(len(strip)):
        if strip[i] and i not in nums:
            return False
    
    for num in nums:
        if not strip[num]:
            return False
    return True
        

def drawDigit(used, posIsDigit):
    strip = [False] * 7
    for char in used:
        for i in range(len(posIsDigit)):
            if char == posIsDigit[i]:
                strip[i] = True

    if onlyNums([0, 1, 2, 4, 5, 6], strip):
        return 0
    elif onlyNums([2, 5], strip):
        return 1
    elif onlyNums([0, 2, 3, 4, 6], strip):
        return 2
    elif onlyNums([0, 2, 3, 5, 6], strip):
        return 3
    elif onlyNums([1, 2, 3, 5], strip):
        return 4
    elif onlyNums([0, 1, 3, 5, 6], strip):
        return 5
    elif onlyNums([0, 1, 3, 4, 5, 6], strip):
        return 6
    elif onlyNums([0, 2, 5], strip):
        return 7
    elif onlyNums([0, 1, 2, 3, 4, 5, 6], strip):
        return 8
    elif onlyNums([0, 1, 2, 3, 5, 6], strip):
        return 9
    

def testGivenPerm(posIsDigit, code):
    seen = [False] * 10
    for c in code:
        num = drawDigit(c, posIsDigit)
        if num is None:
            return False
        seen[num] = True
    
    for s in seen:
        if not s:
            return False
    return True

import itertools
totOut = 0
for i in range(len(lines)):
    l = lines[i].split("|")
    ll = l[1]
    output = ll.split()
    lf = l[0]
    code = lf.split()
    posIsDigit = [0] * 7
    

    perms = list(itertools.permutations(['a', 'b', 'c', 'd', 'e', 'f', 'g']))
    out = 0
    for perm in perms:
        if testGivenPerm(perm, code):
            mult = 1000
            for i in range(len(output)):
                out += drawDigit(output[i], perm) * mult
                mult //= 10
            totOut += out
            break
            
print(totOut)
    
        
        



