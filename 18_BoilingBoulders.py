import math
import copy
import time
from tqdm import tqdm as tqdm #run pip3 install tqdm in terminal

start = time.time()
X = []

with open("0_Data.txt") as fileInput:
    file = list(fileInput)

minmax = [999, 999, 999, 0, 0, 0]
for line in file:
    C = line.strip()
    C = C.split(",")
    C[0] = int(C[0])
    C[1] = int(C[1])
    C[2] = int(C[2])
    minmax = [min(minmax[0], C[0]), min(minmax[1], C[1]), min(minmax[2], C[1]), max(minmax[3], C[0]), max(minmax[4], C[1]), max(minmax[5], C[2])]
    X.append(C)

values = [-1] * (minmax[3] - minmax[0] + 3)
for i in range(len(values)):
    values[i] = [-1] * (minmax[4] - minmax[1] + 3)
    for j in range(len(values[i])):
        values[i][j] = [False] * (minmax[5] - minmax[2] + 3)

run = True
values[0][0][0] = True
#1 means outside, -1 means inside
while run:
    run = False
    for i in range(len(values)):
        for j in range(len(values[i])):
            for k in range(len(values[j])):
                if values[i][j][k]:
                    #0, 0, 0 would go to -1, 0, 0
                    if (i > 0 and not values[i - 1][j][k] and [i - 2, j, k] not in X):
                        run = True
                        values[i - 1][j][k] = True
                        
                    if (i < len(values) - 1 and not values[i + 1][j][k] and [i, j, k] not in X):
                        run = True
                        values[i + 1][j][k] = True
                        
                    if (j > 0 and not values[i][j - 1][k] and [i - 1, j - 1, k] not in X):
                        run = True
                        values[i][j - 1][k] = True
                        
                    if (j < len(values[0]) - 1 and not values[i][j + 1][k] and [i - 1, j + 1, k] not in X):
                        run = True
                        values[i][j + 1][k] = True
                        
                        
                    if (k > 0 and not values[i][j][k - 1] and [i - 1, j, k - 1] not in X):
                        run = True
                        values[i][j][k - 1] = True
                        
                    if (k < len(values[0][0]) - 1 and not values[i][j][k + 1] and [i - 1, j, k + 1] not in X):
                        run = True
                        values[i][j][k + 1] = True
Area = 0
ExternalArea = 0
for i in X:
    x = i[0]
    y = i[1]
    z = i[2]
    if [x - 1, y, z] not in X:
        if values[x][y][z]:
            ExternalArea += 1
        Area += 1
    if [x + 1, y, z] not in X:
        if values[x + 2][y][z]:
            ExternalArea += 1
        Area += 1
        
    if [x, y - 1, z] not in X:
        if values[x + 1][y - 1][z]:
            ExternalArea += 1
        Area += 1
    if [x, y + 1, z] not in X:
        if values[x + 1][y + 1][z]:
            ExternalArea += 1
        Area += 1
        
    if [x, y, z - 1] not in X:
        if values[x + 1][y][z - 1]:
            ExternalArea += 1
        Area += 1
    if [x, y, z + 1] not in X:
        if values[x + 1][y][z + 1]:
            ExternalArea += 1
        Area += 1

print("Part one : " + str(Area))
print("Part one : " + str(ExternalArea))
print("Time : " + str(int((time.time() - start) * 10 + 0.5) / 10.0) + " seconds")