lines = []

with open('input.in') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

mapp = [[x for x in row] for row in lines]

moved = 1
steps = 0
while moved > 0:
    steps += 1
    move = set()
    moved = 0

    for i in range(len(mapp)):
        for j in range(len(mapp[0])):
            if j == len(mapp[0]) - 1:
                if mapp[i][j] == ">" and mapp[i][0] == ".":
                    move.add((i, j))
                    moved += 1
            elif mapp[i][j] == ">" and mapp[i][j+1] == ".":
                move.add((i, j))
                moved += 1

    for (i, j) in move:
        mapp[i][j] = "."
        if j == len(mapp[0]) - 1:
            mapp[i][0] = ">"
        else:
            mapp[i][j+1] = ">"

    move = set()

    for i in range(len(mapp)):
        for j in range(len(mapp[0])):
            if i == len(mapp) - 1:
                if mapp[i][j] == "v" and mapp[0][j] == ".":
                    move.add((i, j))
                    moved += 1
            elif mapp[i][j] == "v" and mapp[i+1][j] == ".":
                move.add((i, j))
                moved += 1

    for (i, j) in move:
        mapp[i][j] = "."
        if i == len(mapp) - 1:
            mapp[0][j] = "v"
        else:
            mapp[i+1][j] = "v"

print(steps)
        