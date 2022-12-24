import math
import copy

X = []

with open("0_Data.txt") as fileInput:
    file = list(fileInput)

for line in file:
    C = line.strip()
    X.append(C)

s = 0
for i in range(int(len(X) / 3)):
    first = []
    second = []
    third = []
    for j in X[3 * i]:
        first.append(j)
    for j in X[3 * i + 1]:
        second.append(j)
    for j in X[3 * i + 2]:
        third.append(j)
    for j in first:
        if (j in second) and (j in third):
            s += 1 + ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'].index(j)
            break

print(s)
            