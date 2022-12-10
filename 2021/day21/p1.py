pos = [7, 5]
score = [0, 0]
die = 1
numThrows = 0
turn = 0

while max(score) < 1000:
    for _ in range(3):
        pos[turn] += die
        die += 1
    while pos[turn] > 10:
        pos[turn] -= 10
    score[turn] += pos[turn]
    turn = 0 if turn == 1 else 1
    numThrows += 3
    

print(min(score) * numThrows)