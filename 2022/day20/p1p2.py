
data = list(map(int, open(0).read().splitlines()))
N = len(data)

def move(nums, indicies, i):
    index = indicies.index(i)
    val = nums[index]
    newIndex = (index + val) % (N - 1)

    nums.pop(index)
    indicies.pop(index)
    nums.insert(newIndex, val)
    indicies.insert(newIndex, i)

def getAns(nums):
    indexZero = nums.index(0)
    return nums[(indexZero+1000)%N] + nums[(indexZero+2000)%N] + nums[(indexZero+3000)%N]

def doPart(part):
    nums = [data[i] * (811589153 if part == 2 else 1) for i in range(N)]
    indicies = [i for i in range(N)]
    
    for _ in range(10 if part == 2 else 1):
        for i in range(N):
            move(nums, indicies, i)
    
    return getAns(nums)

print(doPart(1))
print(doPart(2))