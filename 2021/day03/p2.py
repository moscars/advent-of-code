
lines = []

with open('input.in') as f:
    lines = f.readlines()
    

def getValue(first, lines):
    
    tmp = []
    for line in lines:
        tmp.append(line)
    
    idxPr = 0
    numOnes = 0
    numZero = 0
    while True:
        numOnes = 0
        numZero = 0
        if len(tmp) <= 1:
            return int(tmp[0], 2)
        
        tmp2 = []
        
        for j in range(len(tmp)):
            if tmp[j][idxPr] == "1":
                numOnes += 1
            else:
                numZero += 1
        
        for j in range(len(tmp)):
            if (first and numOnes >= numZero) or (not first and numOnes < numZero):
                if tmp[j][idxPr] == "1":
                    tmp2.append(tmp[j])
            else:
                if tmp[j][idxPr] == "0":
                    tmp2.append(tmp[j])
        idxPr += 1
        tmp = tmp2

first = getValue(True, lines)
second = getValue(False, lines)

print(first, second)
print(first * second)
        


    


        