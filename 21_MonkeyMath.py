#this title is very racist
import math
import copy
import time
from tqdm import tqdm as tqdm

with open("0_Data.txt") as fileInput:
    file = list(fileInput)

start = time.time()
X = []
names = []

for line in file:
    C = line.strip()
    C = C.split(": ")
    if C[0] != "root":
        names.append(C[0])
    try:
        C[1] = int(C[1])
    except:
        match C[1][5]: # +, -, *, / in that order
            case "+":
                C[1] = C[1].split(" + ")
                C.append(0)
            case "-":
                C[1] = C[1].split(" - ")
                C.append(1)
            case "*":
                C[1] = C[1].split(" * ")
                C.append(2)
            case "/":
                C[1] = C[1].split(" / ")
                C.append(3)
            case _:
                print("wtf")
    X.append(C)

names.insert(0, "root")
temp = copy.deepcopy(X)
for i in temp:
    try:
        i[1] = int(i[1])
    except:
        i[1][0] = names.index(i[1][0])
        i[1][1] = names.index(i[1][1])
    name = i.pop(0)
    X[names.index(name)] = i

temp = copy.deepcopy(X)
temp[0][1] = 1 #subtract

def printinstructions():
    for i in range(len(X)):
        try:
            int(X[i][0])
            print(names[i] + " : " + str(X[i][0]))
        except:
            print(names[i] + " : " + str(names[X[i][0][0]]) + " " + ["+", "-", "*", "/"][X[i][1]] + " " + str(names[X[i][0][1]]))

def getmonkey(index):
    if len(X[index]) == 1:
        return X[index][0]
    match X[index][1]:
        case 0:
            X[index] = [getmonkey(X[index][0][0]) + getmonkey(X[index][0][1])]
        case 1:
            X[index] = [getmonkey(X[index][0][0]) - getmonkey(X[index][0][1])]
        case 2:
            X[index] = [getmonkey(X[index][0][0]) * getmonkey(X[index][0][1])]
        case 3:
            X[index] = [float(getmonkey(X[index][0][0]) / getmonkey(X[index][0][1]))]
    return X[index][0]

print("Part one : " + str(int(getmonkey(0))))
print("Time for part one : " + str(int((time.time() - start) * 100) / 1000.0))
print()
start = time.time()

def getmonkeyforparttwo(index):
    if len(X[index]) == 1:
        return X[index][0]
    try:
        int(getmonkeyforparttwo(X[index][0][0]))
        int(getmonkeyforparttwo(X[index][0][1]))
        match X[index][1]:
            case 0:
                X[index] = [getmonkeyforparttwo(X[index][0][0]) + getmonkeyforparttwo(X[index][0][1])]
            case 1:
                X[index] = [getmonkeyforparttwo(X[index][0][0]) - getmonkeyforparttwo(X[index][0][1])]
            case 2:
                X[index] = [getmonkeyforparttwo(X[index][0][0]) * getmonkeyforparttwo(X[index][0][1])]
            case 3:
                X[index] = [float(getmonkeyforparttwo(X[index][0][0]) / getmonkeyforparttwo(X[index][0][1]))]
    except:
        match X[index][1]:
            case 0:
                X[index] = ["(" + str(getmonkeyforparttwo(X[index][0][0])) + " + " + str(getmonkeyforparttwo(X[index][0][1])) + ")"]
            case 1:
                X[index] = ["(" + str(getmonkeyforparttwo(X[index][0][0])) + " - " + str(getmonkeyforparttwo(X[index][0][1])) + ")"]
            case 2:
                X[index] = ["(" + str(getmonkeyforparttwo(X[index][0][0])) + " * " + str(getmonkeyforparttwo(X[index][0][1])) + ")"]
            case 3:
                X[index] = ["(" + str(getmonkeyforparttwo(X[index][0][0])) + " / " + str(getmonkeyforparttwo(X[index][0][1])) + ")"]
    return X[index][0]

X = copy.deepcopy(temp)
X[names.index("humn")] = [0]
zero = getmonkey(0)

larger_index = 1000000000000.0
X = copy.deepcopy(temp)
X[names.index("humn")] = [larger_index]
larger_number = getmonkey(0)

slope = (zero - larger_number) / larger_index

print("Part two : " + str(int(zero / slope)))
print("Time for part two : " + str(int((time.time() - start) * 1000) / 1000.0))
start = time.time()