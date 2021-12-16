
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

def evaluate(typeID, nums):
    if typeID == 0:
        return sum(nums)
    elif typeID == 1:
        val = 1
        for num in nums:
            val *= num
        return val
    elif typeID == 2:
        return min(nums)
    elif typeID == 3:
        return max(nums)
    elif typeID == 5:
        return 1 if nums[0] > nums[1] else 0
    elif typeID == 6:
        return 1 if nums[0] < nums[1] else 0
    elif typeID == 7:
        return 1 if nums[0] == nums[1] else 0
    

def parsePacket():
    global index
    global binary
    index += 3
    typeID = binary[index:index+3]
    index += 3
    typeID = int("0b" + typeID, base=2)
    if typeID == 4:
        num = ""
        while binary[index] == "1":
            index += 1
            num += binary[index:index+4]
            index += 4
        index += 1
        num += binary[index:index+4]
        index += 4
        intNum = int("0b" + num, base=2)
        return intNum
    else:
        lengthTypeID = binary[index]
        if lengthTypeID == "0":
            index += 1
            lengthInBits = binary[index:index+15]
            lengthInt = int("0b" + lengthInBits, base=2)
            index += 15
            ibefore = index
            nums = []
            while index < ibefore + lengthInt:
                nums.append(parsePacket())
            return evaluate(typeID, nums)
        else:
            index += 1
            numContained = binary[index:index+11]
            intNumCont = int("0b" + numContained, base=2)
            index += 11
            nums = []
            while intNumCont > 0:
                nums.append(parsePacket())
                intNumCont -= 1
            return evaluate(typeID, nums)


for char in hexx:
    binary += hexbin[char]


print(parsePacket())

    
            
            
        