import math
import copy
from tqdm import tqdm as tqdm

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

#Part 1
distances = []
ranges = []
height = 2000000 #10 for the example, 2000000 for the actual
beaconsinrange = 0
beaconsinrangex = []
for i in X:
    distance = abs(i[0][0] - i[1][0]) + abs(i[0][1] - i[1][1])
    distances.append(distance)
    r = distance - abs(i[0][1] - height)
    if (r > 0):
        ranges.append([i[0][0] - r, i[0][0] + r])
    if i[1][1] == height:
        if i[1][0] not in beaconsinrangex:
            beaconsinrangex.append(i[1][0])
            beaconsinrange += 1

cr = []
cr1 = []
for i in ranges:
    cr1.append(i[0])
    cr1.sort()
    cr.insert(cr1.index(i[0]), i)
ranges = copy.deepcopy(cr) #Order them

cr = []
start = -1
end = -1
for i in range(len(ranges)):
    if start == -1:
        start = ranges[i][0]
        end = ranges[i][1]
    elif end + 1 >= ranges[i][0]:
        end = max(end, ranges[i][1]) #program views smth like [2, 12] and [2, 8] as the same and will not order them
    else:
        cr.append([start, end])
        start = ranges[i][0]
        end = ranges[i][1]
cr.append([start, end])
ranges = copy.deepcopy(cr) #fix them

target = 0 - beaconsinrange
for i in ranges:
    target += i[1] - i[0] + 1

print("Part one : " + str(target))

#Part 2
def rangeforheight(h):
    distances = []
    ranges = []
    beaconsinrange = 0
    beaconsinrangex = []
    for i in X:
        distance = abs(i[0][0] - i[1][0]) + abs(i[0][1] - i[1][1])
        distances.append(distance)
        r = distance - abs(i[0][1] - h)
        if (r > 0):
            ranges.append([i[0][0] - r, i[0][0] + r])
        if i[1][1] == h:
            if i[1][0] not in beaconsinrangex:
                beaconsinrangex.append(i[1][0])
                beaconsinrange += 1

    cr = []
    cr1 = []
    for i in ranges:
        cr1.append(i[0])
        cr1.sort()
        cr.insert(cr1.index(i[0]), i)
    ranges = copy.deepcopy(cr) #Order them

    cr = []
    start = -1
    end = -1
    for i in range(len(ranges)):
        if start == -1:
            start = ranges[i][0]
            end = ranges[i][1]
        elif end + 1 >= ranges[i][0]:
            end = max(end, ranges[i][1]) #program views smth like [2, 12] and [2, 8] as the same and will not order them
        else:
            cr.append([start, end])
            start = ranges[i][0]
            end = ranges[i][1]
    cr.append([start, end])
    ranges = copy.deepcopy(cr) #fix them
    if len(ranges) > 1:
        print("Part two : " + str(4000000 * (ranges[0][1] + 1) + h))

rangeforheight(3442119)

#for i in tqdm(range(4000000)): rangeforheight(i) #you can do this if you want, it takes roughly 2 mins
                            #you have to run this to get the number though