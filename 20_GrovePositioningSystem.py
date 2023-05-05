import math
from copy import deepcopy
import time
from tqdm import tqdm as tqdm #run pip3 install tqdm in terminal

start = time.time()
X = []
X2 = []

with open("0_Data.txt") as fileInput:
    file = list(fileInput)

for line in file:
    C = line.strip()
    X.append(int(C))
    X2.append(int(C) * 811589153) # 

Grove_Data = []
Grove_Data2 = [] # unfortunately... there are indeed repeated numbers

for i in range(len(X)):
    Grove_Data.append([X[i], i]) # value, order, position
    Grove_Data2.append([X2[i], i]) # value, order, position

toList = [0] * len(Grove_Data)
toList2 = [0] * len(Grove_Data2)

def gdtl():
    global toList, Grove_Data
    for i in Grove_Data:
        toList[i[1]] = i[0]
    for i in Grove_Data2:
        toList2[i[1]] = i[0]

for i in range(len(Grove_Data)):
    final_position = (Grove_Data[i][0] + Grove_Data[i][1]) % (len(Grove_Data) - 1)
    if final_position < 0:
        final_position += len(Grove_Data) - 1
    
    for j in range(len(Grove_Data)):
        # if it's between 
        if final_position <= Grove_Data[j][1] and Grove_Data[j][1] < Grove_Data[i][1]:
            Grove_Data[j][1] += 1
        elif final_position >= Grove_Data[j][1] and Grove_Data[j][1] > Grove_Data[i][1]:
            Grove_Data[j][1] -= 1
    Grove_Data[i][1] = final_position
        
for lmaolmao in tqdm(range(10)):
    for i in range(len(Grove_Data2)):
        final_position = (Grove_Data2[i][0] + Grove_Data2[i][1]) % (len(Grove_Data2) - 1)
        if final_position < 0:
            final_position += len(Grove_Data2) - 1
        
        for j in range(len(Grove_Data2)):
            # if it's between 
            if final_position <= Grove_Data2[j][1] and Grove_Data2[j][1] < Grove_Data2[i][1]:
                Grove_Data2[j][1] += 1
            elif final_position >= Grove_Data2[j][1] and Grove_Data2[j][1] > Grove_Data2[i][1]:
                Grove_Data2[j][1] -= 1
        Grove_Data2[i][1] = final_position


gdtl()

t = toList.index(0)
t2 = toList2.index(0)

print("Part One: " + str(toList[(t + 1000) % len(toList)] + toList[(t + 2000) % len(toList)] + toList[(t + 3000) % len(toList)]))
print("Part Two: " + str(toList2[(t2 + 1000) % len(toList2)] + toList2[(t2 + 2000) % len(toList2)] + toList2[(t2 + 3000) % len(toList2)]))
print("Total Runtime: " + str(int((time.time() - start) * 100 + 0.5) / 100)) # takes around 100 seconds in total