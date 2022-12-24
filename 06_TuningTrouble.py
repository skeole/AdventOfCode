import math
import copy

X = []

with open("0_Data.txt") as fileInput:
    file = list(fileInput)

for line in file:
    C = line.strip()
    X.append(C)

string = X[0]

print(len(string))

last = ['0']
for i in range(13):
    last.append(string[i])

for i in range(13, len(string)):
    last.pop(0)
    last.append(string[i])
    boolean = True
    t = copy.deepcopy(last)
    for j in range(14):
        a = t.pop(0)
        if a in t:
            boolean = False
    if boolean:
        print(i + 1)
        break