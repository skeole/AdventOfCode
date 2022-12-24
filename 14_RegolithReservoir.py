import math
import copy

X = []

with open("0_Data.txt") as fileInput:
    file = list(fileInput)

ymin = 0
ymax = 0
xmin = 0
xmax = 0
for line in file:
    C = line.strip()
    C = C.split(" -> ")
    X.append([])
    for i in range(len(C)):
        C[i] = C[i].split(",")
        C[i][0] = int(C[i][0]) - 500
        C[i][1] = int(C[i][1])
        xmin = min(xmin, C[i][0])
        xmax = max(xmax, C[i][0])
        ymax = max(ymax, C[i][1])
        X[len(X) - 1].append(C[i])

xmin -= ymax
xmax -= xmin
xmax += ymax
ymax += 2
startpoint = [0 - xmin, 0]

for i in range(len(X)):
    for j in range(len(X[i])):
        X[i][j][0] -= xmin

sofar = []
for i in range(xmax + 1):
    sofar.append([0] * (ymax + 1))
    sofar[i][ymax] = 1

sofar[startpoint[0]][startpoint[1]] = -1
for i in X:
    prev = i[0]
    for j in i:
        if prev[0] > j[0]:
            for k in range(j[0], prev[0] + 1):
                sofar[k][j[1]] = 1
        elif prev[0] < j[0]:
            for k in range(prev[0], j[0] + 1):
                sofar[k][j[1]] = 1
        elif prev[1] > j[1]:
            for k in range(j[1], prev[1] + 1):
                sofar[j[0]][k] = 1
        elif prev[1] < j[1]:
            for k in range(prev[1], j[1] + 1):
                sofar[j[0]][k] = 1
        else:
            sofar[j[0]][j[1]] = 1
        prev = j

def smartprint(arr):
    for i in range(len(arr[0])):
        s = ""
        for j in range(max(0, startpoint[0] - 30), min(startpoint[0] + 31, len(arr))):
            if arr[j][i] == 2:
                s += "o"
            elif arr[j][i] == 1:
                s += "#"
            elif arr[j][i] == 0:
                s += "."
            elif arr[j][i] == -1:
                s += "+"
        print(s)
    print()

def tick():
    global r
    sandpos = copy.deepcopy(startpoint)
    run = True
    while (run):
        if sandpos[1] + 1 == len(sofar[0]):
            r = False
            run = False
        elif sofar[sandpos[0]][sandpos[1] + 1] == 0:
            sandpos[1] += 1
        elif sofar[sandpos[0] - 1][sandpos[1] + 1] == 0:
            sandpos[1] += 1
            sandpos[0] -= 1
        elif sofar[sandpos[0] + 1][sandpos[1] + 1] == 0:
            sandpos[1] += 1
            sandpos[0] += 1
        else:
            if sandpos == startpoint:
                r = False
            run = False
    sofar[sandpos[0]][sandpos[1]] = 2

r = True
counter = 0
while(r):
    tick()
    counter += 1

smartprint(sofar)
print(counter)