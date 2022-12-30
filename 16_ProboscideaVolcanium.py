import math
import copy
from tqdm import tqdm as tqdm
import time

a = time.time()

X = []

with open("0_Data.txt") as fileInput:
    file = list(fileInput)

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
t = []

for line in file:
    C = line.strip()
    s = ""
    for i in range(6, len(C)):
        s += C[i]
    C = s
    C = C.split(" has flow rate=")
    try:
        C[1].index("; tunnels lead to valves ")
        C[1] = C[1].split("; tunnels lead to valves ")
    except:
        C[1] = C[1].split("; tunnel leads to valve ")
    C[1][1] = C[1][1].split(", ")
    C[0] = 26 * alphabet.index(C[0][0]) + alphabet.index(C[0][1])
    t.append(C[0])
    C[1][0] = int(C[1][0])
    for i in range(len(C[1][1])):
        C[1][1][i] = 26 * alphabet.index(C[1][1][i][0]) + alphabet.index(C[1][1][i][1])
    X.append([C[0], C[1][0], C[1][1]])

t.sort()

for i in range(len(X)):
    X[i][0] = t.index(X[i][0])
    for j in range(len(X[i][2])):
        X[i][2][j] = t.index(X[i][2][j])

class valve(object):
    def __init__(self, rate, tunnels):
        self.active = False
        if rate == 0:
            self.active = True
        self.rate = rate
        self.tunnels = tunnels

valves = [0] * len(t)
for i in X:
    valves[i[0]] = valve(i[1], i[2])
valves[0].active = False

def indexFromValves(v1, v2):
    return int(max(v1, v2) * max(v1 - 1, v2 - 1) / 2.0) + min(v1, v2)

distances = [999] * int(len(X) * (len(X) - 1) / 2.0)

index = 0
for i in range(len(valves)): #target
    run = True
    while (run):
        run = False #if there are any changes, run becomes true
        for j in range(len(valves)):
            if i != j:
                index = indexFromValves(i, j)
                calc = 999
                for k in valves[j].tunnels:
                    if k == i:
                        calc = 1
                    else:
                        calc = min(calc, distances[indexFromValves(i, k)] + 1)
                if (distances[index] > calc):
                    distances[index] = calc
                    run = True

for i in range(len(distances)):
    distances[i] += 1 #caching the distances between ALL pairs

temp1 = copy.deepcopy(valves)
temp2 = copy.deepcopy(distances)
temp3 = []
for i in range(len(temp1)):
    if not temp1[i].active:
        temp3.append(i)
        
valves = []
distances = [0] * int(len(temp3) * (len(temp3) - 1) / 2.0)
for i in temp3:
    valves.append(temp1[i])
    for j in temp3:
        if not i == j:
            distances[indexFromValves(temp3.index(i), temp3.index(j))] = temp2[indexFromValves(i, j)]

#Part one code here

cachedresults = [0] * len(valves)
for i in range(len(valves)):
    cachedresults[i] = [0] * 31
    for j in range(31):
        cachedresults[i][j] = [-1] * (2 ** len(valves))

def debinary(number):
    l = 0
    s = 0
    for i in number:
        if i:
            s += (2 ** l)
        l += 1
    return s

def score(position, actives, timeleft): #we can either sit tight, or we can go to an inactive position and activate it
    global cachedresults
    temp = copy.deepcopy(actives)
    temp[position] = True #because it is activated
    
    if timeleft <= 0:
        return 0
    
    t1 = debinary(temp)
    
    if cachedresults[position][timeleft][t1] != -1:
        return cachedresults[position][timeleft][t1]
    
    ticker = 0
    for i in range(len(temp)):
        if temp[i]:
            ticker += valves[i].rate
    
    tempscore = ticker * timeleft #ABSOLUTE MINIMUM they can get, if they just sit
    
    for i in range(len(temp)):
        if not temp[i]: #if we aren't active
            dist = distances[indexFromValves(i, position)]
            if (timeleft >= dist):
                tempscore = max(tempscore, score(i, temp, timeleft - dist) + ticker * dist)
    
    cachedresults[position][timeleft][t1] = tempscore
    
    return tempscore

print("Part one : " + str(score(0, [False] * len(valves), 30)))
print("Part one runtime : " + str(int((time.time() - a) * 100 + 0.5) / 100))
print()

#Part two
#26 minutes, but 2 people

#Okay. Que es nuestro plan por parte dos
#I don't think bashing will work here
#However - i believe there is more than enough time to go to every location
#PERHAPS
#We divide it into 2 sections then add them

#But - which one will work the best?
indices1 = []
indices2 = []

valves1 = []
trueorfalse = []
cachedresults1 = []
distances1 = []

def resetstate(indices):
    global cachedresults1, valves1, distances1, trueorfalse
    if indices.count(0) == 0:
        indices.insert(0, 0)
    t = len(indices)
    cachedresults1 = [0] * t
    for i in range(t):
        cachedresults1[i] = [0] * 31
        for j in range(31):
            cachedresults1[i][j] = [-1] * (2 ** t)
            
    valves1 = []
    distances1 = [0] * int(t * (t - 1) / 2.0)

    for i in indices:
        valves1.append(valves[i])
        for j in indices:
            if not i == j:
                distances1[indexFromValves(indices.index(i), indices.index(j))] = distances[indexFromValves(i, j)]
    
    trueorfalse = [False] * t

def score1(position, actives, timeleft):
    global cachedresults1
    temp = copy.deepcopy(actives)
    temp[position] = True #because it is activated
    
    if timeleft <= 0:
        return 0
    
    t1 = debinary(temp)
    
    if cachedresults1[position][timeleft][t1] != -1:
        return cachedresults1[position][timeleft][t1]
    
    ticker = 0
    for i in range(len(temp)):
        if temp[i]:
            ticker += valves1[i].rate
    
    tempscore = ticker * timeleft #ABSOLUTE MINIMUM they can get, if they just sit
    
    for i in range(len(temp)):
        if not temp[i]: #if we aren't active
            dist = distances1[indexFromValves(i, position)]
            if (timeleft >= dist):
                tempscore = max(tempscore, score1(i, temp, timeleft - dist) + ticker * dist)
    
    cachedresults1[position][timeleft][t1] = tempscore
    
    return tempscore

def binary(number, length=(len(valves) - 2)):
    s = []
    for i in range(length):
        if number % 2 == 0:
            s.insert(0, False)
        else:
            s.insert(0, True)
        number = int(number / 2)
    return s

def count(number, length=(len(valves) - 2)):
    s = 0
    for i in range(length):
        if number % 2 == 0:
            s += 1
        number = int(number / 2)
    return s / (len(valves) - 1)

def findscore(binarynumber):
    global indices1, indices2
    indices1 = [0, 1]
    indices2 = [0]
    t = binary(binarynumber)
    for i in range(len(t)):
        if t[i]:
            indices1.append(i + 2)
        else:
            indices2.append(i + 2)
    resetstate(indices1)
    s = score1(0, trueorfalse, 26)
    resetstate(indices2)
    s += score1(0, trueorfalse, 26)
    return s

m = 0
for i in tqdm(range(2 ** (len(valves) - 2))):
    if (count(i) > 0.4) and (count(i) < 0.6): #kind of cheating, remove this restriction if the answer isn't correct 
                #(technically you can invert it to save some time)
                #The total time without such a restriction should be around 9 minutes
        m = max(findscore(i), m)

print("Part two : " + str(m))