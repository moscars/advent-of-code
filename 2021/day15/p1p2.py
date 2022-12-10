from queue import PriorityQueue

lines = []

with open('input.in') as f:
    lines = f.readlines()

def dijkstras(p2=False):
    graph = [[int(x) for x in line.strip()] for line in lines]

    if p2:
        g1 = []
        for row in graph:
            r = []
            for i in range(5):
                for num in row:
                    r.append(num + i)
            g1.append(r)


        g2 = []
        for i in range(5):
            for row in g1:
                newRow = []
                for elem in row:
                    add = elem + i
                    if add >= 10:
                        add -= 9
                    newRow.append(add)
                g2.append(newRow)

        graph = g2
        
    cost = [[float("inf") for _ in range(len(graph[0]))] for _ in range(len(graph))]

    q = PriorityQueue()
    q.put((0, 0, 0))
    while not q.empty():
        c, i, j = q.get()
        n = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
        for ii, jj in n:
            if 0 <= ii < len(graph[0]) and 0 <= jj < len(graph):
                newC = c + graph[ii][jj]
                if newC < cost[ii][jj]:
                    cost[ii][jj] = newC
                    q.put((newC, ii, jj))
    return cost[-1][-1]

print(dijkstras())
print(dijkstras(True))
    
    

