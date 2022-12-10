
lines = []

with open('input.in') as f:
    lines = f.readlines()

hexx = lines[0]
binary = ""

hexbin = {
    "0" : "0000",
    "1" : "0001",
    "2" : "0010",
    "3" : "0011",
    "4" : "0100",
    "5" : "0101",
    "6" : "0110",
    "7" : "0111",
    "8" : "1000",
    "9" : "1001",
    "A" : "1010",
    "B" : "1011",
    "C" : "1100",
    "D" : "1101",
    "E" : "1110",
    "F" : "1111"
}
index = 0
tot = 0

def parsePacket():
    global index
    global tot
    global binary
    version = binary[index:index+3]
    intVersion = int("0b" + version, base=2)
    tot += intVersion
    index += 3
    typeID = binary[index:index+3]
    index += 3
    if typeID == "100":
        num = ""
        while binary[index] == "1":
            index += 1
            num += binary[index:index+4]
            index += 4
        index += 1
        num += binary[index:index+4]
        index += 4
    else:
        lengthTypeID = binary[index]
        if lengthTypeID == "0":
            index += 1
            lengthInBits = binary[index:index+15]
            lengthInt = int("0b" + lengthInBits, base=2)
            index += 15
            ibefore = index
            while index < ibefore + lengthInt:
                parsePacket()
        else:
            index += 1
            numContained = binary[index:index+11]
            intNumCont = int("0b" + numContained, base=2)
            index += 11
            while intNumCont > 0:
                parsePacket()
                intNumCont -= 1


for char in hexx:
    binary += hexbin[char]

parsePacket()

print(tot)


    
            
            
        