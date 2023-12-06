import re

lines = open(0).read().splitlines()

times = list(map(int, re.findall(r'\d+', lines[0])))
distances = list(map(int, re.findall(r'\d+', lines[1])))

times2 = [int("".join([str(i) for i in times]))]
distances2 = [int("".join([str(i) for i in distances]))]

timesParts = [times, times2]
distancesParts = [distances, distances2]

def good(hold, targetDist, totTime):
    timeLeft = totTime - hold
    dist = timeLeft * hold
    return dist > targetDist

def lowerBound(targetDist, lo, hi, totTime):
    best = None
    while lo <= hi:
        mid = (lo + hi) // 2
        if good(mid, targetDist, totTime):
            hi = mid - 1
            best = mid
        else:
            lo = mid + 1
    return best

def upperBound(targetDist, lo, hi, totTime):
    best = None
    while lo <= hi:
        mid = (lo + hi) // 2
        if good(mid, targetDist, totTime):
            lo = mid + 1
            best = mid
        else:
            hi = mid - 1
    return best

for (times, distances) in zip(timesParts, distancesParts):
    ans = 1
    for race in range(len(times)):
        time = times[race]
        firstGood = lowerBound(distances[race], 0, time // 2, time)
        lastGood = upperBound(distances[race], time // 2, time, time)
        ans *= (lastGood - firstGood + 1)

    print(ans)