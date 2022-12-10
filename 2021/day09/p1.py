
lines = []

with open('input.in') as f:
    lines = f.readlines()

mapp = []

for line in lines:
    row = []
    for char in line.strip():
        row.append(int(char))
    mapp.append(row)
    

tot = 0
for i in range(len(mapp)):
    for j in range(len(mapp[0])):
        c = mapp[i][j]
        low = True
        if i - 1 >= 0 and mapp[i-1][j] <= c:
            low = False
        if j - 1 >= 0 and mapp[i][j-1] <= c:
            low = False
        if j + 1 <= len(mapp[0]) - 1 and mapp[i][j+1] <= c:
            low = False
        if i + 1 <= len(mapp) - 1 and mapp[i+1][j] <= c:
            low = False
        if low:
            tot += c + 1

print(tot)