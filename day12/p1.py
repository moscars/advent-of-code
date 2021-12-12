
lines = []

with open('input.in') as f:
    lines = f.readlines()

adjList = {}

tot = 0
from collections import deque

def bfs():
    global tot
    q = deque()
    q.append(("start", ["start"]))
    while q:
        curr, path = q.popleft()
        
        if curr == "end":
            tot += 1
            continue
       
        for neigh in adjList[curr]:
            np = [elem for elem in path]
            if neigh not in np or neigh.isupper():
                np.append(neigh)
                q.append((neigh, np))

for line in lines:
    l = line.split("-")
    fromm = l[0].strip()
    to = l[1].strip()
    
    if fromm not in adjList:
        adjList[fromm] = []
    
    if to not in adjList:
        adjList[to] = []
    
    adjList[fromm].append(to)
    adjList[to].append(fromm)

bfs()
print(tot)

    

            
            
        