import math
import copy

X = []

with open("0_Data.txt") as fileInput:
    file = list(fileInput)

for line in file:
    C = line.strip()
    C = C.split()
    for i in range(int(C[1])):
        X.append(C[0])

H = []
for i in range(10):
    H.append([0, 0])
#Rules:
#H - T Vector:
#If 2, 0: T moves [1, 0]
#If 2, 1: T moves [1, 1]
PastPositions = [[0, 0]]

def tick(direction):
    match direction:
        case "U":
            H[0][1] += 1
        case "D":
            H[0][1] -= 1
        case "L":
            H[0][0] -= 1
        case "R":
            H[0][0] += 1
    for i in range(9):
        if abs(H[i][0] - H[i + 1][0]) + abs(H[i][1] - H[i + 1][1]) > 2:
            if (H[i][0] > H[i + 1][0]):
                H[i + 1][0] += 1
            else:
                H[i + 1][0] -= 1
            if (H[i][1] > H[i + 1][1]):
                H[i + 1][1] += 1
            else:
                H[i + 1][1] -= 1
        elif H[i][0] > H[i + 1][0] + 1:
            H[i + 1][0] += 1
        elif H[i][0] < H[i + 1][0] - 1:
            H[i + 1][0] -= 1
        elif H[i][1] > H[i + 1][1] + 1:
            H[i + 1][1] += 1
        elif H[i][1] < H[i + 1][1] - 1:
            H[i + 1][1] -= 1

for i in X:
    tick(i)
    if H[9] not in PastPositions:
        PastPositions.append(copy.deepcopy(H[9]))

print(len(PastPositions))