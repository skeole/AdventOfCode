import math
import copy
from tqdm import tqdm as tqdm

X = []

with open("0_Data.txt") as fileInput:
    file = list(fileInput)

for line in file:
    C = line.strip()
    X.append(C)

pattern = X[0]
counter = 0
height_of_bottom = 0
rock_number = 0
formation = []
totalheight = 0

numrocks = 2022

def reset(rock):
    global totalheight
    
    fixedrock = []
    for j in range(max(0, len(rock) - 50), len(rock)): #kinda cheating but... i do not care :)
        fixedrock.append(copy.deepcopy(rock[j]))
    
    totalheight += len(rock) - len(fixedrock)
    return fixedrock

def printrock(rock):
    for i in range(len(rock) - 1, max(-1, len(rock) - 50), -1):
        s = "|"
        for j in rock[i]:
            if j:
                s += "#"
            else:
                s += "."
        s += "|"
        print(s)
    s = "+"
    for i in range(len(rock[0])):
        s += "-"
    s += "+"
    print(s)
    print()

def printrock2(rock, yeet):
    global totalheight
    temp = totalheight
    rock = combine(rock, yeet)
    totalheight = temp
    for i in range(len(rock) - 1, max(-1, len(rock) - 50), -1):
        s = "|"
        for j in range(len(rock[i])):
            if rock[i][j]:
                if [j, i] in yeet:
                    s += "@"
                else:
                    s += "#"
            else:
                s += "."
        s += "|"
        print(s)
    s = "+"
    for i in range(len(rock[0])):
        s += "-"
    s += "+"
    print(s)
    print()

def intersect(rock, positions):
    for i in positions:
        try:
            if rock[i[1]][i[0]]:
                return True
        except:
            if i[1] <= 0:
                return True
            pass
    return False

def change(positions, vector):
    t = copy.deepcopy(positions)
    for i in range(len(t)):
        t[i][0] += vector[0]
        t[i][1] += vector[1]
    return t

def combine(rock, positions):
    t = copy.deepcopy(rock)
    for i in positions:
        while len(t) <= i[1]: 
            #ex. if the length is 2 and we're at y=3, we want go to until length = 4
            t.append([False] * 7)
        t[i[1]][i[0]] = True
    t = reset(t)
    return t

def minimax(positions):
    mini = 999
    maxi = 0
    for i in positions:
        mini = min(mini, i[0])
        maxi = max(maxi, i[0])
    return [mini, maxi]

print()
steights = []
yes = True
cycle = -1
heights = []
difference = -1

for i in tqdm(range(numrocks)): #i = 0 --> after 1 rock; i == 2021 --> after 2022 rocks
    CauseImFreeFallin = True
    min_height = len(formation) + 3
    if formation == []:
        min_height = 3
        formation = [[False] * 7]
    match (i % 5):
        case 0:
            fallingrock = [[2, min_height], [3, min_height], [4, min_height], [5, min_height]]
        case 1:
            fallingrock = [[3, min_height], [2, min_height + 1], [3, min_height + 1], [4, min_height + 1], [3, min_height + 2]]
        case 2:
            fallingrock = [[2, min_height], [3, min_height], [4, min_height], [4, min_height + 1], [4, min_height + 2]]
        case 3:
            fallingrock = [[2, min_height], [2, min_height + 1], [2, min_height + 2], [2, min_height + 3]]
        case 4:
            fallingrock = [[2, min_height], [3, min_height], [2, min_height + 1], [3, min_height + 1]]
    
    while (CauseImFreeFallin):
        jet_sweep = pattern[counter]
        
        if (jet_sweep == ">"):
            if (minimax(fallingrock)[1] < 6):
                fallingrock = change(fallingrock, [1, 0])
                if intersect(formation, fallingrock):
                    fallingrock = change(fallingrock, [-1, 0])
        
        elif (minimax(fallingrock)[0] > 0):
            fallingrock = change(fallingrock, [-1, 0])
            if intersect(formation, fallingrock):
                fallingrock = change(fallingrock, [1, 0])
        
        fallingrock = change(fallingrock, [0, -1])
        CauseImFreeFallin = not intersect(formation, fallingrock)
        if fallingrock[0][1] == -1:
            CauseImFreeFallin = False
        
        if not CauseImFreeFallin:
            fallingrock = change(fallingrock, [0, 1])
        
        counter += 1
        counter %= len(pattern)
    
    formation = combine(formation, fallingrock)
    state = [i % 5, counter, formation]
    if yes and (state not in steights):
        heights.append(totalheight + len(formation))
        steights.append(state)
    elif yes:
        yes = False
        tempo = steights.index(state)
        cycle = i - tempo
        difference = totalheight + len(formation) - heights[tempo]
        tempoheights = [0] * cycle
        for j in range(tempo, i):
            tempoheights[j % cycle] = heights[j]
        heights = copy.deepcopy(tempoheights)
    
    if i == 2021:
        th1 = totalheight + len(formation)

def heightat(pos):
    temp = heights[(pos - 1) % len(heights)] + difference * int((pos - 1 - tempo) / len(heights))
    return str(temp)

print()
print("Part one : " + str(th1))
print("Part two : " + heightat(1000000000000))
#printrock(formation)