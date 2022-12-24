import math
import copy

X = []

with open("0_Data.txt") as fileInput:
    file = list(fileInput)

for line in file:
    C = line.strip()
    C = C.split(",")
    C[0] = C[0].split("-")
    C[1] = C[1].split("-")
    C[0][0] = int(C[0][0])
    C[0][1] = int(C[0][1])
    C[1][0] = int(C[1][0])
    C[1][1] = int(C[1][1])
    X.append(C)

print(X)

c = 0
for i in X:
    if (i[0][1] >= i[1][0] >= i[0][0]) or (i[1][1] >= i[0][0] >= i[1][0]):
        c += 1

print(c)