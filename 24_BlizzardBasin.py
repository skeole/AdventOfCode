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
    C = C.strip("#")
    if len(C) != 1:
        X.append(C)

# There are 25 rows and 120 columns
# There are 3002 spaces for us and 600 possibilities for where the storm is, which means only 1801200 datapoints

# In the example, there are 4 rows and 6 columns
# 26 spaces and 12 possibilities for where the storm is, which means only 312 datapoints

# I'm lazy but the gcf is just the square root of the first one loel

def free_at_time(x, y, time):
    # X[y][x] is the character at x, y
    if (y == -1) or y == len(X):
        return True
    if X[(y - time) % len(X)][x] == "v":
        return False
    if X[(y + time) % len(X)][x] == "^":
        return False
    if X[y][(x - time) % len(X[0])] == ">":
        return False
    if X[y][(x + time) % len(X[0])] == "<":
        return False
    return True

def adjacent_moves(x, y):
    if y == -1:
        return [[0, -1], [0, 0]]
    if y == len(X):
        return [[len(X[0]) - 1, len(X)], [len(X[0]) - 1, len(X) - 1]]
    adj_moves = [[x, y]]
    if x > 0:
        adj_moves.append([x - 1, y])
    if x < len(X[0]) - 1:
        adj_moves.append([x + 1, y])
    if y > 0:
        adj_moves.append([x, y - 1])
    if y < len(X) - 1:
        adj_moves.append([x, y + 1])
    return adj_moves

data = []
example = False
if len(X) == 4:
    data = [9999] * 312 # 12 * 26
    example = True
elif len(X) == 25:
    data = [9999] * 1801200 # 3002 * 600

def data_to_index(x, y, day):
    pos = -1
    if y == -1:
        pos = len(X) * len(X[0])
    elif y == len(X):
        pos = len(X) * len(X[0]) + 1
    else:
        pos = x * len(X) + y # len(X[0]) - 1, len(X) - 1 -> yeah
    
    if example:
        return (day % 12) * 26 + pos
    else:  
        return (day % 600) * 3002 + pos

def index_to_data(index):
    if example:
        pos = index % 26
        day = int(index / 26)
        if pos == 24:
            return [0, -1, day]
        elif pos == 25:
            return [0, len(X), day]
        else:
            return [int(pos / len(X)), pos % len(X), day]
    else:
        pos = index % 3002
        day = int(index / 3002)
        if pos == 3000:
            return [0, -1, day]
        elif pos == 3001:
            return [0, len(X), day]
        else:
            return [int(pos / len(X)), pos % len(X), day]

def iter():
    global data
    data2 = [9999] * len(data)
    for i in range(len(data)):
        if data[i] != 9999:
            t = index_to_data(i)
            assert (t[2] - data[i]) % 12 == 0
            for move in adjacent_moves(t[0], t[1]):
                if (free_at_time(move[0], move[1], data[i] + 1)):
                    data2[data_to_index(move[0], move[1], t[2] + 1)] = min(data[i] + 1, data[data_to_index(move[0], move[1], t[2] + 1)])
    data = data2

data[data_to_index(0, -1, 0)] = 0

run = True

tim = 0
while run:
    iter()
    if example:
        for i in range(24):
            if data[data_to_index(len(X[0]) - 1, len(X) - 1, i)] != 9999:
                run = False
    else:
        for i in range(600):
            if data[data_to_index(len(X[0]) - 1, len(X) - 1, i)] != 9999:
                run = False
    
    tim += 1
    if tim % 10 == 0:
        print(tim)

tim += 1

part_one_ans = str(tim)
part_one_runtime = str(int((time.time() - start) * 100 + 0.5) / 100)
start = time.time()

data = []
example = False
if len(X) == 4:
    data = [9999] * 312 # 12 * 26
    example = True
elif len(X) == 25:
    data = [9999] * 1801200 # 3002 * 600
    
data[data_to_index(len(X[0]) - 1, len(X), tim)] = tim
run = True

while run:
    iter()
    if example:
        for i in range(24):
            if data[data_to_index(0, 0, i)] != 9999:
                run = False
    else:
        for i in range(600):
            if data[data_to_index(0, 0, i)] != 9999:
                run = False
    
    tim += 1
    if tim % 10 == 0:
        print(tim)

tim += 1

data = []
example = False
if len(X) == 4:
    data = [9999] * 312 # 12 * 26
    example = True
elif len(X) == 25:
    data = [9999] * 1801200 # 3002 * 600
data[data_to_index(0, -1, tim)] = tim

run = True

while run:
    iter()
    if example:
        for i in range(24):
            if data[data_to_index(len(X[0]) - 1, len(X) - 1, i)] != 9999:
                run = False
    else:
        for i in range(600):
            if data[data_to_index(len(X[0]) - 1, len(X) - 1, i)] != 9999:
                run = False
    
    tim += 1
    if tim % 10 == 0:
        print(tim)

tim += 1

print()
print("Part One Answer: " + part_one_ans)
print("Part One Runtime : " + part_one_runtime) # should take around 40 seconds
print()
print("Part Two Answer: " + str(tim))
print("Part Two Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100)) # lol this was such a weird day but this should take around 80 seconds