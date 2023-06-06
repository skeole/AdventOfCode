import math
from copy import deepcopy
import time
from tqdm import tqdm as tqdm #run pip3 install tqdm in terminal

start = time.time()
X = []

with open("0_Data.txt") as fileInput:
    file = list(fileInput)

for line in file:
    C = line.strip()
    X.append(C)

elves = []
for i in range(len(X)):
    for j in range(len(X[i])):
        if X[i][j] == "#":
            elves.append([j, len(X) - 1 - i])

grid = [0] * len(X)
for i in range(len(grid)):
    grid[i] = [-1] * len(X[0]) # otherwise it has the index of the elf

for i in range(len(elves)):
    grid[elves[i][1]][elves[i][0]] = i



def expand(dir): # 0 means N, 1 means S, 2 means W, 3 means E
    global min_row, min_col
    if dir == 0:
        grid.append([-1] * len(grid[0]))
    elif dir == 1:
        min_row -= 1
        grid.insert(0, [-1] * len(grid[0]))
    elif dir == 2:
        min_col -= 1
        for i in range(len(grid)):
            grid[i].insert(0, -1)
    elif dir == 3:
        for i in range(len(grid)):
            grid[i].append(-1)



def smartprint():
    grid.reverse()
    for i in grid:
        string = ""
        for j in i:
            if j == -1:
                string += "."
            else:
                string += "#"
        print(string)
    grid.reverse()
    print()

min_row = 0
min_col = 0 # basically this is how we convert the location of the elves into the grid. 

# if our elf is at (3, 4) and the min_row is -5 and min_col is -2, then the position is (3 + 2, 4 + 5) = (5, 9) in the grid
# and vice versa

def char_at(x, y):
    adj_x = x - min_col
    adj_y = y - min_row
    
    if adj_x < 0:
        expand(2)
        return -1
    elif adj_x >= len(grid[0]):
        expand(3)
        return -1
    elif adj_y < 0:
        expand(1)
        return -1
    elif adj_y >= len(grid):
        expand(0)
        return -1
    
    return grid[adj_y][adj_x]

def set_char(x, y, val):
    grid[y - min_row][x - min_col] = val

proposed_moves = [0] * len(elves)
for i in range(len(proposed_moves)):
    proposed_moves[i] = [0, 0]

def propose_moves(turn): # 0 means N, 1 means S, 2 means W, 3 means E
    move = turn % 4
    for i in range(len(elves)):
        neighbors = [
            char_at(elves[i][0], elves[i][1] + 1) == -1, 
            char_at(elves[i][0] + 1, elves[i][1] + 1) == -1, 
            char_at(elves[i][0] + 1, elves[i][1]) == -1, 
            char_at(elves[i][0] + 1, elves[i][1] - 1) == -1, 
            char_at(elves[i][0], elves[i][1] - 1) == -1, 
            char_at(elves[i][0] - 1, elves[i][1] - 1) == -1, 
            char_at(elves[i][0] - 1, elves[i][1]) == -1, 
            char_at(elves[i][0] - 1, elves[i][1] + 1) == -1
        ]
        
        nswe = [
            (neighbors[-1] and neighbors[0] and neighbors[1]), 
            (neighbors[3] and neighbors[4] and neighbors[5]), 
            (neighbors[5] and neighbors[6] and neighbors[7]), 
            (neighbors[1] and neighbors[2] and neighbors[3])
        ]
        
        nswepos = [
            [elves[i][0], elves[i][1] + 1], 
            [elves[i][0], elves[i][1] - 1], 
            [elves[i][0] - 1, elves[i][1]], 
            [elves[i][0] + 1, elves[i][1]]
        ]
        
        if nswe[0] and nswe[1] and nswe[2] and nswe[3]:
            proposed_moves[i][0] = elves[i][0]
            proposed_moves[i][1] = elves[i][1]
        elif nswe[move]:
            proposed_moves[i][0] = nswepos[move][0]
            proposed_moves[i][1] = nswepos[move][1]
        elif nswe[move - 3]:
            proposed_moves[i][0] = nswepos[move - 3][0]
            proposed_moves[i][1] = nswepos[move - 3][1]
        elif nswe[move - 2]:
            proposed_moves[i][0] = nswepos[move - 2][0]
            proposed_moves[i][1] = nswepos[move - 2][1]
        elif nswe[move - 1]:
            proposed_moves[i][0] = nswepos[move - 1][0]
            proposed_moves[i][1] = nswepos[move - 1][1]
        else:
            proposed_moves[i][0] = elves[i][0]
            proposed_moves[i][1] = elves[i][1]

def act_on_proposed_moves():
    constant = True
    for i in range(len(proposed_moves)):
        if char_at(proposed_moves[i][0], proposed_moves[i][1]) == -1:
            constant = False
            set_char(proposed_moves[i][0], proposed_moves[i][1], i)
            set_char(elves[i][0], elves[i][1], -1)
            elves[i][0] = proposed_moves[i][0]
            elves[i][1] = proposed_moves[i][1]
        elif (proposed_moves[i][0] != elves[i][0]) or (proposed_moves[i][1] != elves[i][1]):
            constant = False
            elves[char_at(proposed_moves[i][0], proposed_moves[i][1])] = [2 * proposed_moves[i][0] - elves[i][0], 2 * proposed_moves[i][1] - elves[i][1]]
            set_char(2 * proposed_moves[i][0] - elves[i][0], 2 * proposed_moves[i][1] - elves[i][1], char_at(proposed_moves[i][0], proposed_moves[i][1]))
            set_char(proposed_moves[i][0], proposed_moves[i][1], -1)
    if constant:
        1 / 0

count = 0
score = 0
while True:
    propose_moves(count)
    try:
        act_on_proposed_moves()
    except Exception:
        count += 1
        break
    count += 1
    if count == 10:
        minx = 100
        maxx = 0
        miny = 100
        maxy = 0
        for i in elves:
            minx = min(minx, i[0])
            maxx = max(maxx, i[0])
            miny = min(miny, i[1])
            maxy = max(maxy, i[1])
        score = (maxx - minx + 1) * (maxy - miny + 1) - len(elves)
        print("Part One Answer: " + str(score))
        print("Part One Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))
        start = time.time()
        print()

print("Part Two Answer: " + str(count))
print("Part Two Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100)) # should take around 15 seconds at most