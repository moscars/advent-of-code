lines = open(0).read().splitlines()

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def checkIndex(line, i, part):
    if line[i] in "0123456789":
        return int(line[i])

    if part == 2:
        for digit in digits:
            if line[i:i+len(digit)] == digit:
                return digits.index(digit) + 1
        
    return None

def getFirst(line, part=1):
    for i in range(len(line)):
        found = checkIndex(line, i, part)
        if found:
            return found
                
def getLast(line, part=1):
    for i in range(len(line) - 1, -1, -1):
        found = checkIndex(line, i, part)
        if found:
            return found

p1, p2 = 0, 0
for line in lines:
    firstP1 = getFirst(line)
    lastP1 = getLast(line)
    firstP2 = getFirst(line, part=2)
    lastP2 = getLast(line, part=2)
    p1 += int(str(firstP1) + str(lastP1))
    p2 += int(str(firstP2) + str(lastP2))

print(p1)
print(p2)