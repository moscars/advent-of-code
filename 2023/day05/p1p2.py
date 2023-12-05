
groups = open(0).read().split("\n\n")
seeds = list(map(int, groups[0].split(": ")[1].split()))

def getNewRange(current, convert):
    if len(current) == 0:
        return []
    new, extra = [], []
    for start, finish in current:
        for startSource, startDest, length in convert:
            finishC = startSource + length

            if startSource <= start <= finish <= finishC:
                diff = start - startSource
                overlap = finish - start
                new.append((startDest + diff, startDest + diff + overlap))
                break

            elif startSource <= start <= finishC < finish:
                diff = start - startSource
                overlap = finishC - start
                new.append((startDest + diff, startDest + diff + overlap))
                extra.append((finishC + 1, finish))
                break
            
            elif start < startSource <= finish <= finishC:
                overlap = finish - startSource
                new.append((startDest, startDest + overlap))
                extra.append((start, startSource - 1))
                break
        else:
            new.append((start, finish))

    new.extend(getNewRange(extra, convert))
    return new

p1, p2 = [], []
for i in range(0, len(seeds), 2):
    p2.append((seeds[i], seeds[i] + seeds[i + 1] - 1))
    p1.extend([(seeds[i], seeds[i]), (seeds[i+1], seeds[i+1])])
    
for i, group in enumerate(groups[1:]):
    lines = group.splitlines()[1:]

    convert = []
    for line in lines:
        dest, source, length = map(int, line.strip().split())
        convert.append((source, dest, length))
    p1 = getNewRange(p1, convert)
    p2 = getNewRange(p2, convert)

print(min([x[0] for x in p1]))
print(min([x[0] for x in p2]))