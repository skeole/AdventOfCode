import math
import copy

#Starting from day 15, I'll have it show both answers in the form:
#Part 1 : [answer]
#Part 2 : [answer]
#I'll add this for the previous days later

X = []

with open("0_Data.txt") as fileInput:
    file = list(fileInput)

for line in file:
    C = line.strip()
    C = C.strip("Sensor at x=")
    C = C.split(": closest beacon is at x=")
    C[0] = C[0].split(", y=")
    C[0][0] = int(C[0][0])
    C[0][1] = int(C[0][1])
    C[1] = C[1].split(", y=")
    C[1][0] = int(C[1][0])
    C[1][1] = int(C[1][1])
    X.append(C)

print(X)