import re
import math

lines = []

pattern = re.compile('\d\d+')

with open('input.in') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]
    
nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
def sumOfSnailNums(snail1, snail2):
    res = "[" + snail1 + "," + snail2 + "]"
    split = True
    explode = True
    while split or explode:
        index = 0
        depth = 0
        split = False
        explode = False
        #check for explosion
        while index < len(res):
            if split or explode:
                break
            if res[index] == "[":
                depth += 1
            elif res[index] == "]":
                depth -= 1
            if depth == 5:
                if res[index] in nums:
                    explode = True
                    n1 = ""
                    start = index
                    while res[index] != ",":
                        n1 += res[index]
                        index += 1
                    n2 = ""
                    index += 1
                    while res[index] != "]":
                        n2 += res[index]
                        index += 1
                    num2 = int(n2)
                    num1 = int(n1)
                    foundNum = True
                    while res[index] not in nums:
                        if index + 1 >= len(res):
                            foundNum = False
                            break
                        index += 1
                    
                    if foundNum:
                        numToMakeBiggerA = ""
                        startHere = index
                        while res[index] in nums:
                            numToMakeBiggerA += res[index]
                            index += 1
                        rest = res[index:]
                        beginning = res[:startHere]
                        numToMakeBiggerA = str(int(numToMakeBiggerA) + num2)
                        
                        res = beginning + numToMakeBiggerA + rest
                        index = startHere - 1
                    
                    while index >= start:
                        index -= 1
                        
                    foundNum = True
                    while res[index] not in nums:
                        if index - 1 < 0:
                            foundNum = False
                            break
                        index -= 1
                    if foundNum:
                        numToMakeBiggerB = ""
                        startHere = index
                        while res[index] in nums:
                            numToMakeBiggerB += res[index]
                            index -= 1
                        numToMakeBiggerB = numToMakeBiggerB[::-1]
                        rest = res[startHere + 1:]
                        beginning = res[:index + 1]
                        numToMakeBiggerB = str(int(numToMakeBiggerB) + num1)
                        res = beginning + numToMakeBiggerB + rest
                        index += 1
                    while True:
                        if res[index] == "[" and res[index+1] not in ["[", ","]:
                            break
                        index += 1
                    index += 1
                    beginning = res[:index - 1]
                    while res[index] != "]":
                        index += 1
                    rest = res[index + 1:]
                    res = beginning + "0" + rest
            index += 1
        #check for split
        if not explode:
            matches = re.finditer(pattern, res)
            for match in matches:
                startIndex = match.start(0)
                endIndex = match.end(0)
                num = float(res[startIndex:endIndex])
                before = res[:startIndex]
                after = res[endIndex:]
                first = int(num // 2)
                second = int(math.ceil(num / 2))
                res = before + "[" + str(first) + "," + str(second) + "]" + after
                split = True
                break
    return res


def magn(res):
    try:
        num = int(res)
        return num   
    except:
        depth = 0
        for i, char in enumerate(res):
            if char == "[":
                depth += 1
            elif char == "]":
                depth -= 1
            elif char == "," and depth == 1:
                first = res[1:i]
                second = res[i+1:len(res)-1]
                return 3 * magn(first) + 2 * magn(second)
    
s = sumOfSnailNums(lines[0], lines[1])
for i in range(2, len(lines)):
    s = sumOfSnailNums(s, lines[i])

print(magn(s))

maxx = 0
for i in range(len(lines)):
    for j in range(len(lines)):
        if i != j:
            m = magn(sumOfSnailNums(lines[i], lines[j]))
            if m > maxx: maxx = m

print(maxx)


    

        

    
            
            
        