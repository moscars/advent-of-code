
lines = []

with open('input.in') as f:
    lines = f.readlines()

mapp = []

for line in lines:
    row = []
    for char in line.strip():
        row.append(int(char))
    mapp.append(row)

seen = [[False for i in range(len(mapp[0]))] for j in range(len(mapp))]

def dfs(mapp, i, j, size):
    global seen
    if i < 0 or i >= len(mapp) or j < 0 or j >= len(mapp[0]) or seen[i][j] or mapp[i][j] == 9:
        return size

    seen[i][j] = True
    size += 1
    
    size += dfs(mapp, i+1, j, 0)
    size += dfs(mapp, i-1, j, 0)
    size += dfs(mapp, i, j+1, 0)
    size += dfs(mapp, i, j-1, 0)
    return size

top3 = []
for i in range(len(mapp)):
    for j in range(len(mapp[0])):
        c = mapp[i][j]
        maxHere = dfs(mapp, i, j, 0)
        if maxHere != 0:
            top3.append(maxHere)
    
top3.sort(reverse=True)
print(top3[0] * top3[1] * top3[2])