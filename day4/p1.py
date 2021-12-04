
def checkBoard(board):
    for row in board:
        allTrue = True
        for elem in row:
            if not elem[1]:
                allTrue = False
        if allTrue:
            return True
    for j in range(5):
        allTrue = True
        for i in range(5):
            if not board[i][j][1]:
                allTrue = False
        if allTrue:
            return True
    return False
                
def updateBoard(board, num):
    for i in range(5):
        for j in range(5):
            if board[i][j][0] == num:
                board[i][j][1] = True
    return board

def calcOut(board):
    summ = 0
    for row in board:
        for num in row:
            if not num[1]:
                summ += num[0]
    return summ
    
    


lines = []

with open('input.in') as f:
    lines = f.readlines()

boards = []

order = lines[0].split(',')
for i in range(len(order)):
    order[i] = int(order[i])

lines.pop(0)
board = []
for line in lines:
    line = line.strip()
    if len(line) > 1:
        board.append(line.split())
    else:
        boards.append(board)
        board = []

boards.append(board)
boards2 = []
for board in boards:
    if len(board) > 3:
        boards2.append(board)
boards = boards2
for i in range(len(boards)):
    for j in range(5):
        for k in range(5):
            boards[i][j][k] = [int(boards[i][j][k]), False]

done = False
for num in order:
    if done:
        break
    for i in range(len(boards)):
        boards[i] = updateBoard(boards[i], num)
    for board in boards:
        if checkBoard(board):
            print(calcOut(board) * num)
            done = True
            break
        