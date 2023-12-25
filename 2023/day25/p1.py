import networkx as nx

lines = open(0).read().splitlines()

G = nx.DiGraph()
vertices = set()
for line in lines:
    from_, rest = line.split(": ")
    rest = rest.split()
    vertices.add(from_)

    for to_ in rest:
        G.add_edge(from_, to_, capacity=1)
        G.add_edge(to_, from_, capacity=1)
        vertices.add(to_)

vertices = list(vertices)
for v1, v2 in zip(vertices, vertices[1:]):
    cut, p = nx.minimum_cut(G, v1, v2)
    if cut == 3:
        print(len(p[0]) * len(p[1]))
        exit()