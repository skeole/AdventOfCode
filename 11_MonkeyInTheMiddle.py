import math
import copy
from tqdm import tqdm as tqdm #run pip3 install tqdm in terminal

X = []

with open("0_Data.txt") as fileInput:
    file = list(fileInput)

file.append("")

index = 0
for line in file:
    C = line.strip()
    C = C.split()
    X.append(C)

def funct(start, operator, number):
    if operator == "+":
        return int(start) + int(number)
    if number == "old":
        return int(start) * int(start)
    return int(start) * int(number)

lcm = 1

class monke(object):
    def __init__(self, startingitems, op1, op2, test, true, false):
        global lcm
        self.num = 0
        lcm *= int(test)
        self.test = int(test)
        self.items = startingitems
        self.operation1 = op1
        self.operation2 = op2
        self.TrueMonke = int(true)
        self.FalseMonke = int(false)
    
    def tick(self):
        for i in self.items:
            self.num += 1
            k = funct(i, self.operation1, self.operation2)
            if (k % self.test == 0):
                monkes[self.TrueMonke].items.append(k % lcm)
            else:
                monkes[self.FalseMonke].items.append(k % lcm)
        self.items = []

monkes = []
temp = []
op1 = ""
op2 = ""
testNum = 0
tm = 0
fm = 0

for line in X:
    if line == []:
        monkes.append(monke(temp, op1, op2, testNum, tm, fm))
        temp = []
    elif line[0] == "Starting":
        for i in range(2, len(line)):
            temp.append(int(line[i].split(",")[0]))
    elif line[0] == "Operation:":
        op1 = line[4]
        op2 = line[5]
    elif line[0] == "Test:":
        testNum = int(line[3])
    elif line[1] == "true:":
        tm = int(line[5])
    elif line[1] == "false:":
        fm = int(line[5])

def printMonkes():
    for i in monkes:
        print(i.items)
    print()

def printMonkes2():
    for i in monkes:
        print(i.num)
    print()

printMonkes()

def tock():
    for i in monkes:
        i.tick()

for i in tqdm(range(10000)):
    tock()

printMonkes2()