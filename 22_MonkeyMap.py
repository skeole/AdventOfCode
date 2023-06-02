import math
from copy import deepcopy
import time
from tqdm import tqdm as tqdm #run pip3 install tqdm in terminal

start = time.time()
X = []

with open("0_Data.txt") as fileInput:
    file = list(fileInput)

for line in file:
    C = line.strip("\n") # Beginning spaces are relevant for this problem
    X.append(C)

direction = 1 # R is 1, U is 0, D is 2, L is 3
temp = X[-1].split("R")
for i in range(len(temp)):
    temp[i] = temp[i].split("L")
    for j in range(len(temp[i])):
        temp[i][j] = int(temp[i][j])

X.pop()
X.pop()

row_wraparounds = [] # this is muy ez to do
column_wraparounds = [] # this is less ez to do

maxlen = 0
for i in X:
    maxlen = max(maxlen, len(i) - 1)
    first = i.index(".")
    last = len(i) - 1
    if "#" in i and first > i.index("#"): # this means we can't wraparound right
        row_wraparounds.append([last, last])
    elif i[last] == "#": # this means we can't wraparound left
        row_wraparounds.append([first, first])
    else:
        row_wraparounds.append([last, first])

for i in range(maxlen):
    count = 0
    while len(X[count]) <= i or X[count][i] == " ":
        count += 1 # we stop once X[count][i] is not whitespace
    first = count
    
    while count < len(X) and (len(X[count]) > i and X[count][i] != " "):
        count += 1 # we stop once X[count][i] is whitespace or is out of bounds
    count -= 1
    if X[first][i] == "#":
        column_wraparounds.append([count, count])
    elif X[count][i] == "#":
        column_wraparounds.append([first, first])
    else:
        column_wraparounds.append([count, first])

pos = [X[0].index("."), 0]

def smartprint(t):
    for j in t:
        print(j)

def smartprint2(t, j):
    strink = ""
    for row in range(len(t)):
        for column in range(len(t[row])):
            if row == j[1] and column == j[0]:
                strink += "X"
            else:
                strink += t[row][column]
        print(strink)
        strink = ""

def smartprint3(t):
    for i in t:
        strink = ""
        for j in i:
            strink += j
        print(strink)
        strink = ""

# Part One
''' Rules
Wraparound
Stop once we hit a wall 
Note that our final row/column is one plus whatever the index is '''

# ok so basically how it goes

for i in temp:
    for j in i: # j is num steps
        for step in range(j):
            if direction == 1:
                pos[0] += 1
                if pos[0] == len(X[pos[1]]):
                    pos[0] = row_wraparounds[pos[1]][1]
                elif X[pos[1]][pos[0]] == "#":
                    pos[0] -= 1
            elif direction == 3:
                pos[0] -= 1
                if pos[0] == -1 or X[pos[1]][pos[0]] == " ":
                    pos[0] = row_wraparounds[pos[1]][0]
                elif X[pos[1]][pos[0]] == "#":
                    pos[0] += 1
            elif direction == 2:
                pos[1] += 1
                if pos[1] == len(X) or len(X[pos[1]]) <= pos[0] or X[pos[1]][pos[0]] == " ":
                    pos[1] = column_wraparounds[pos[0]][1]
                elif X[pos[1]][pos[0]] == "#":
                    pos[1] -= 1
            elif direction == 0:
                pos[1] -= 1
                if pos[1] == -1 or len(X[pos[1]]) <= pos[0] or X[pos[1]][pos[0]] == " ":
                    pos[1] = column_wraparounds[pos[0]][0]
                elif X[pos[1]][pos[0]] == "#":
                    pos[1] += 1
        
        direction = (direction - 1) % 4
    direction = (direction + 2) % 4 # add two because we subtract one too many times

direction = (direction - 2) % 4
print("Part One Answer: " + str(1000 * (pos[1] + 1) + 4 * (pos[0] + 1) + direction))
print("Part One Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))
start = time.time()
print()

# For part two, do the same thing except wraparounds are more difficult

# Okay... let's try to make a general solution

# Basically, we have concave corners and they mirror each other until both sides are convex

# our thing will be the new row, new column, and the new direction

# We have concave when we turn right and convex when we turn left

# len(k) - len(k.strip()) is the amount of whitespace at the beginning

but_im_not_a_wrapper = [len(X[0]) - len(X[0].strip()), 0]
last_dir = 2

border = [[deepcopy(but_im_not_a_wrapper), last_dir]] # R is 1, U is 0, D is 2, L is 3
first = True

def check(array, position): # position is x, y
    if (position[1] < 0 or position[0] < 0):
        return False
    try:
        return array[position[1]][position[0]] != " "
    except Exception:
        return False
    
concavities = []
rohangodha = 0

while (but_im_not_a_wrapper != [len(X[0]) - len(X[0].strip()), 0]) or first:
    rohangodha += 1
    
    testconcavepos = [but_im_not_a_wrapper[0], but_im_not_a_wrapper[1]]
    
    testconvexpos = [but_im_not_a_wrapper[0], but_im_not_a_wrapper[1]]
    
    if last_dir == 2:
        but_im_not_a_wrapper[0] += 1
        testconcavepos[0] += 1
        testconcavepos[1] -= 1
    elif last_dir == 3:
        but_im_not_a_wrapper[1] += 1
        testconcavepos[0] += 1
        testconcavepos[1] += 1
    elif last_dir == 0:
        but_im_not_a_wrapper[0] -= 1
        testconcavepos[0] -= 1
        testconcavepos[1] += 1
    elif last_dir == 1:
        but_im_not_a_wrapper[1] -= 1
        testconcavepos[0] -= 1
        testconcavepos[1] -= 1
    
    # if testconcavepos exists -> concave
    # new direction -> -= 1
    # if we're whitespace or nonexistent -> convex
    # new direction -> += 1
    
    if check(X, testconcavepos):
        but_im_not_a_wrapper = deepcopy(testconcavepos)
        last_dir = (last_dir - 1) % 4
        concavities.append(rohangodha)
        
    elif check(X, but_im_not_a_wrapper):
        pass
    else:
        but_im_not_a_wrapper = deepcopy(testconvexpos)
        last_dir = (last_dir + 1) % 4
    
    border.append([deepcopy(but_im_not_a_wrapper), last_dir])
    
    first = False

# Im fucking lazy ok
matches1 = []
matches2 = []

for i in concavities:
    lower = i - 1
    upper = i
    first = True
    length = 0
    
    matches1.append([border[lower][0], (border[lower][1] + 2) % 4])
    matches1.append([border[upper][0], (border[upper][1] + 2) % 4])
    matches2.append(border[upper])
    matches2.append(border[lower])
        
    while ((border[lower][1] == border[lower + 1][1]) or (border[upper][1] == border[upper - 1][1])) or first:
        length += 1
        first = False
        lower -= 1
        upper = (upper + 1) % len(border)
        
        matches1.append([border[lower][0], (border[lower][1] + 2) % 4])
        matches1.append([border[upper][0], (border[upper][1] + 2) % 4])
        matches2.append(border[upper])
        matches2.append(border[lower])

pos = [X[0].index("."), 0]
direction = 1
for i in temp:
    for j in i: # j is num steps

        for step in range(j):
            
            prev_pos = [deepcopy(pos), direction]
            if direction == 1:
                pos[0] += 1
            elif direction == 3:
                pos[0] -= 1
            elif direction == 2:
                pos[1] += 1
            elif direction == 0:
                pos[1] -= 1
            
            if not check(X, pos):
                pos = deepcopy(matches2[matches1.index(prev_pos)][0])
                direction = matches2[matches1.index(prev_pos)][1]
            
            if X[pos[1]][pos[0]] == "#":
                pos = deepcopy(prev_pos[0])
                direction = prev_pos[1]
                
        direction = (direction - 1) % 4
        
    direction = (direction + 2) % 4 # add two because we subtract one too many times

direction = (direction - 2) % 4

print("Part Two Answer: " + str(1000 * (pos[1] + 1) + 4 * (pos[0] + 1) + direction))
print("Part Two Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100)) # LFGGGGG