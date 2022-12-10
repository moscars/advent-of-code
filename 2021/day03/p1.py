
lines = []

with open('input.in') as f:
    lines = f.readlines()

gamma = ""
epsilon = ""
print(len(lines[0]))
print(len(lines))
for i in range(len(lines[0])-1):
    numOnes = 0
    numZero = 0
    for j in range(len(lines)):
        print(i, j)
        if lines[j][i] == "1":
            numOnes += 1
        else:
            numZero += 1
    if numOnes > numZero:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"
    
g = int(gamma, 2)
e = int(epsilon, 2)
print(g * e)


        