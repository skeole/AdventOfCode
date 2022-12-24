import math
import copy

X = []

with open("0_Data.txt") as fileInput:
    file = list(fileInput)

for line in file:
    C = line.strip()
    X.append(C)

c1 = 0
c2 = 0
c3 = 0
t = 0
for i in X:
    if i == "":
        if t > c1:
            c1 = t
        elif t > c2:
            c2 = t
        elif t > c3:
            c3 = t
        t = 0
    else:
        t += int(i)


if t > c1:
    c1 = t
elif t > c2:
    c2 = t
elif t > c3:
    c3 = t
print(c1 + c2 + c3)