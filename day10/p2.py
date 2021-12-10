
lines = []

with open('input.in') as f:
    lines = f.readlines()

stack = []

openn = ["(", "[", "{", "<"]
match = {")": "(", "]": "[", "}":"{",">": "<"}
points = {"(": 1, "[": 2, "{" : 3, "<": 4}

scores = []
for line in lines:
    stack = []
    scoreHere = 0
    cont = False
    for char in line.strip():
        if char in openn:
            stack.append(char)
        else:
            top = stack.pop()
            if top != match[char]:
                cont = True
                break
    if cont:
        continue
    for i in range(len(stack) - 1, -1, -1):
        scoreHere *= 5
        scoreHere += points[stack[i]]
    scores.append(scoreHere)
        
scores.sort()      
print(scores[len(scores) // 2])
            
            
        