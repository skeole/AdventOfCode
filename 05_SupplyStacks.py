import math
import copy

X = []

with open("0_Data.txt") as fileInput:
    file = list(fileInput)

boxes = []
for i in range(9):
    boxes.append([])
instructions = []
t = True
for line in file:
    C = line.strip()
    if t:
        if C == "":
            t = False
        else:
            if C[0] != "1":
                x = 1
                for i in range(9):
                    try:
                        if line[x] != " ":
                            boxes[i].append(line[x])
                    except:
                        pass
                    x += 4
    else:
        C = C.split()
        instructions.append([int(C[1]), int(C[3]), int(C[5])])

print(boxes)
print(instructions)

for i in instructions:
    for j in range(i[0]):
        a = boxes[i[1] - 1].pop(0)
        boxes[i[2] - 1].insert(j, a)

str = ""
for i in boxes:
    try:
        str += i[0]
    except:
        pass

print(str)