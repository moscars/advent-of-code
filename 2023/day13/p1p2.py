chunks = open(0).read().split("\n\n")

def checkSymmetry(g, blocked):
    for i in range(len(g) - 1):
        if i == blocked:
            continue

        good = True
        prev = i
        nxt = i + 1
        while prev >= 0 and nxt < len(g):
            if g[prev] != g[nxt]:
                good = False
                break
            prev -= 1
            nxt += 1

        if good:
            return i + 1
    
    return 0

def checkGraph(g, blockedHorizontal, blockedVertical):
    return checkSymmetry(g, blockedHorizontal), checkSymmetry(list(zip(*g)), blockedVertical)

def other(c):
    return "." if c == "#" else "#"

graphs = []
p1 = 0
for chunk in chunks:
    g = [list(line) for line in chunk.splitlines()]

    horizontal, vertical = checkGraph(g, None, None)
    graphs.append((g, horizontal, vertical))

totHor, totVer = 0, 0
for g, horizontal, vertical in graphs:
    found = False
    for i in range(len(g)):
        if found:
            break
        for j in range(len(g[0])):
            g[i][j] = other(g[i][j])

            hor, ver = checkGraph(g, horizontal - 1, vertical - 1)
            if hor or ver:
                totHor += hor
                totVer += ver
                found = True
                break
        
            g[i][j] = other(g[i][j])


p1 = sum(g[1] for g in graphs) * 100 + sum(g[2] for g in graphs)
p2 = totHor * 100 + totVer

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")