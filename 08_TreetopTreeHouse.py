import math
import copy

X = []

with open("0_Data.txt") as fileInput:
    file = list(fileInput)

for line in file:
    C = line.strip()
    C = list(C)
    for i in range(len(C)):
        C[i] = int(C[i])
    X.append(C)

maxscore = 0
for i in range(len(X)):
    for j in range(len(X[i])):
        score = 1
        height = X[i][j]
        
        temp = True
        temp1 = 0
        for k in range(i - 1, -1, -1):
            if (temp):
                temp1 += 1
                if X[k][j] >= height:
                    temp = False
        score *= temp1
        
        temp = True
        temp1 = 0
        for k in range(i + 1, len(X)):
            if (temp):
                temp1 += 1
                if X[k][j] >= height:
                    temp = False
        score *= temp1
        
        temp = True
        temp1 = 0
        for k in range(j - 1, -1, -1):
            if (temp):
                temp1 += 1
                if X[i][k] >= height:
                    temp = False
        score *= temp1
        
        temp = True
        temp1 = 0
        for k in range(j + 1, len(X)):
            if (temp):
                temp1 += 1
                if X[i][k] >= height:
                    temp = False
        score *= temp1
        
        maxscore = max(maxscore, score)

print(maxscore)