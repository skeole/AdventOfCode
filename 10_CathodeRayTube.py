import math
import copy

X = []

with open("0_Data.txt") as fileInput:
    file = list(fileInput)

for line in file:
    C = line.strip()
    C = C.split()
    X.append(0)
    if len(C) == 2:
        X.append(int(C[1]))

position = 1
row = -1

matrix = []

for i in range(len(X)):
    if i % 40 == 0:
        row += 1
        matrix.append([])
    #before step i
    if abs(position - (i % 40)) < 2:
        matrix[row].append("#")
    else:
        matrix[row].append(".")
    
    position += X[i]

for i in matrix:
    s = ""
    raw = ""
    for j in i:
        raw += j
        if j == "#":
            s += "00"
        else:
            s += "  "
    print(s)
    #print(raw)