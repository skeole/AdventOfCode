import math
import copy
from tqdm import tqdm as tqdm

X = []

with open("0_Data.txt") as fileInput:
    file = list(fileInput)

file.append("")

for line in file:
    C = line.strip()
    if C != "":
        X.append(C)

def parseArrayString(arrayString):
    arr = []
    temp = ""
    i = 1
    while (i < len(arrayString) - 1):
        if arrayString[i] == "[":
            temp = ""
            count = 1
            stri = "["
            while (count > 0):
                i += 1
                if arrayString[i] == "[":
                    count += 1
                elif arrayString[i] == "]":
                    count -= 1
                stri += arrayString[i]
            i += 1 #to get past the comma
            arr.append(parseArrayString(stri))
        elif arrayString[i] == ",":
            arr.append(int(temp))
            temp = ""
        else:
            temp += arrayString[i] 
        i += 1
    if temp != "":
        arr.append(int(temp))
    return arr

for i in range(len(X)):
    X[i] = parseArrayString(X[i])

def compareArrays(arr1, arr2):
    x = min(len(arr1), len(arr2))
    for i in range(x):
        if (type(arr1[i]) == type(arr2[i]) == int):
            if arr1[i] > arr2[i]:
                return False
            elif arr1[i] < arr2[i]:
                return True
        else:
            t1 = copy.deepcopy(arr1[i])
            t2 = copy.deepcopy(arr2[i])
            if (type(t1) == int):
                t1 = [t1]
            if (type(t2) == int):
                t2 = [t2]
            if (compareArrays(t1, t2)):
                return True
            if (compareArrays(t2, t1)):
                return False
        #2 cases: both integers or at least one is an array
    if len(arr2) > len(arr1):
        return True
    return False

X.append([[2]])
X.append([[6]])

print(X)
run = True

k = 0
while(run):
    run = False
    k += 1
    print(k)
    for i in range(len(X) - 1):
        if compareArrays(X[i + 1], X[i]):
            t1 = copy.deepcopy(X[i])
            t2 = copy.deepcopy(X[i + 1])
            X[i] = t2
            X[i + 1] = t1
            run = True
            

print(X.index([[2]]) + 1)
print(X.index([[6]]) + 1)
    