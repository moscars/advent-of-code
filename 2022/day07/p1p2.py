import sys

data = sys.stdin.read()
lines = data.splitlines()

class Node:
    def __init__(self):
        self.children = {}
        self.parent = None
        self.files = []

def createTree():
    tree = Node()
    curr = tree

    totalUsed = 0
    for line in lines:
        c = line.split()
        if c[0] == '$':
            if c[1] == 'cd':
                if c[2] == '/':
                    curr = tree
                elif c[2] == '..':
                    curr = curr.parent
                else:
                    curr = curr.children[c[2]]
        elif c[0] == 'dir':
            node = Node()
            curr.children[c[1]] = node
            node.parent = curr
        else:
            curr.files.append(int(c[0]))
            totalUsed += int(c[0])
    return tree, totalUsed

sizes = []
def calcSum(node):
    size = sum([calcSum(s) for s in node.children.values()]) + sum(node.files)
    sizes.append(size)
    return size

tree, totalUsed = createTree()
left = 70000000 - totalUsed
toBeDeleted = 30000000 - left
calcSum(tree)
print(sum([s for s in sizes if s <= 100000]))
print(min([s for s in sizes if s >= toBeDeleted]))