
lines = open(0).read().splitlines()

dp = {}
def getAllPossible(pattern, nums, i, j, lenCurr):
    state = (i, j, lenCurr)
    if state in dp:
        return dp[state]

    if i >= len(pattern):
        if j >= len(nums):
            return 1
        else:
            if j == len(nums) - 1:
                return lenCurr == nums[j]
            else:
                return 0
                
    need = nums[j] if j < len(nums) else None

    ans = 0
    if pattern[i] == "?":
        # we play #
        if need is not None and lenCurr + 1 <= need:
            ans += getAllPossible(pattern, nums, i + 1, j, lenCurr + 1)
        
        # we play .
        if lenCurr > 0 and lenCurr == need:
            ans += getAllPossible(pattern, nums, i + 1, j + 1, 0)
        elif lenCurr == 0:
            ans += getAllPossible(pattern, nums, i + 1, j, 0)
    
    elif pattern[i] == "#":
        if need is not None and lenCurr + 1 <= need:
            ans = getAllPossible(pattern, nums, i + 1, j, lenCurr + 1)
    else:
        if lenCurr > 0 and lenCurr == need:
            ans = getAllPossible(pattern, nums, i + 1, j + 1, 0)
        elif lenCurr == 0:
            ans =  getAllPossible(pattern, nums, i + 1, j, 0)

    dp[state] = ans
    return ans

p1, p2 = 0, 0
for line in lines:
    pattern, nums = line.split()
    nums = list(map(int, nums.split(",")))

    dp.clear()
    p1 += getAllPossible(pattern, nums, 0, 0, 0)
    dp.clear()
    p2 += getAllPossible("?".join([pattern] * 5), nums * 5, 0, 0, 0)

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")