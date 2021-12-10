
lines = []

with open('input.in') as f:
    lines = f.readlines()

stack = []

openn = ["(", "[", "{", "<"]
match = {")": "(", "]": "[", "}":"{",">": "<"}
points = {")": 3, "]": 57, "}" : 1197, ">": 25137}

tot = 0
for line in lines:
    for char in line.strip():
        if char in openn:
            stack.append(char)
        else:
            top = stack.pop()
            if match[char] != top:
                tot += points[char]
                break
                
print(tot)
            
            
        