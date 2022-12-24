import math
import copy

X = []

with open("0_Data.txt") as fileInput:
    file = list(fileInput)

alphabet = list("abcdefghijklmnopqrstuvwxyz")

num = 0
start = [0, 0]
target = [0, 0]
for line in file:
    C = line.strip()
    C = list(C)
    X.append([])
    for i in range(len(C)):
        if C[i] == "S":
            start = [num, i]
            X[num].append(0)
        elif C[i] == "E":
            target = [num, i]
            X[num].append(25)
        else:
            X[num].append(alphabet.index(C[i]))
    num += 1

def smartprint(array):
    for i in array:
        s = ""
        for j in i:
            s += str(j)
            s += "\t"
        print(s)
    print()
        
fib = [-1] * len(X)
for i in range(len(fib)):
    fib[i] = [-1] * len(X[0])

fib[target[0]][target[1]] = 0

def tick():
    global fib
    #HOW TO GO IN REVERSE:
        #We can go up any amount of altitude
        #We can go down a maximum of ONE
        #value += 1
    for i in range(len(fib)):
        for j in range(len(fib[i])):
            if fib[i][j] != -1: #if it's been initialized
                if (i > 0) and (X[i - 1][j] + 2 > X[i][j]) and ((fib[i - 1][j] == -1) or (fib[i - 1][j] > fib[i][j])):
                    fib[i - 1][j] = fib[i][j] + 1
                
                if (i < len(fib) - 1) and (X[i + 1][j] + 2 > X[i][j]) and ((fib[i + 1][j] == -1) or (fib[i + 1][j] > fib[i][j])):
                    fib[i + 1][j] = fib[i][j] + 1
                    
                if (j > 0) and (X[i][j - 1] + 2 > X[i][j]) and ((fib[i][j - 1] == -1) or (fib[i][j - 1] > fib[i][j])):
                    fib[i][j - 1] = fib[i][j] + 1
                    
                if (j < len(fib[0]) - 1) and (X[i][j + 1] + 2 > X[i][j]) and ((fib[i][j + 1] == -1) or (fib[i][j + 1] > fib[i][j])):
                    fib[i][j + 1] = fib[i][j] + 1

while (fib[start[0]][start[1]] == -1):
    tick()

m = fib[start[0]][start[1]]
for i in range(len(X)):
    for j in range(len(X[i])):
        if X[i][j] == 0:
            if fib[i][j] != -1:
                m = min(m, fib[i][j])

print(m)

