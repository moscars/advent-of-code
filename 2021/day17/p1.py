
lines = []

with open('input.in') as f:
    lines = f.readlines()

line = lines[0].strip().split()

xs = line[2].split("x=")[1].split("..")
ys = line[3].split("y=")[1].split("..")

x1 = int(xs[0])
x2 = int(xs[1][0:len(xs[1]) - 1])
y1 = int(ys[0])
y2 = int(ys[1])

maxY = 0

def evaluate(xvel, yvel):
    global maxY
    x = 0
    y = 0
    localMax = 0
    while y > y1:
        x += xvel
        y += yvel
        if y > localMax: 
            localMax = y
        if xvel > 0: xvel -= 1
        if xvel < 0: xvel += 1
        yvel -= 1
        if x1 <= x <= x2 and y1 <= y <= y2:
            if localMax > maxY:
                maxY = localMax

for x in range(20):
    for y in range(200):
        evaluate(x, y)

print(maxY)

        

    
            
            
        