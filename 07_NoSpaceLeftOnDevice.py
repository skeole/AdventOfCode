import math
import copy

X = []

with open("0_Data.txt") as fileInput:
    file = list(fileInput)

for line in file:
    C = line.strip()
    C = C.split()
    X.append(C)

tab = "  "

class directory(object):
    def __init__(self, name):
        self.files = []
        self.directories = []
        self.directorynames = []
        self.name = name
        
    def getSize(self):
        s = 0
        for i in self.files:
            s += i.getSize()
        for i in self.directories:
            s += i.getSize()
        return s
    
    def printDirectory(self, numIndents=0):
        s = ""
        for i in range(numIndents):
            s += tab
        print(s + " - " + self.name + " (dir, total size = " + str(self.getSize()) + ")")
        for i in self.files:
            i.printFile(numIndents + 1)
        for i in self.directories:
            i.printDirectory(numIndents + 1)
            
    def addDirectory(self, location, name):
        l = copy.deepcopy(location)
        if len(l) != 1:
            l.pop(0)
            self.directories[self.directorynames.index(l[0])].addDirectory(l, name)
        else:
            self.directorynames.append(name)
            self.directories.append(directory(name))
            
    def addFile(self, location, name, size):
        l = copy.deepcopy(location)
        if len(l) != 1:
            l.pop(0)
            self.directories[self.directorynames.index(l[0])].addFile(l, name, size)
        else:
            self.files.append(file(name, size))
    
    def addSmallFiles(self, s=0):
        sui = 0
        if self.getSize() <= 100000:
            sui += self.getSize()
        for i in self.directories:
            sui += i.addSmallFiles(s = sui)
        return sui
    
    def allDirectorySizes(self):
        sizes = [self.getSize()]
        for i in self.directories:
            j = i.allDirectorySizes()
            for k in j:
                sizes.append(k)
        return sizes
            

class file(object):
    def __init__(self, name, size):
        self.name = name
        self.size = int(size) #im stupid lmao
        
    def getSize(self):
        return self.size
    
    def printFile(self, numIndents):
        s = ""
        for i in range(numIndents):
            s += tab
        print(s + " - " + self.name + " (file, size = " + str(self.size) + ")")

main = directory("/")
location = []

for i in X:
    if i[0] == "$":
        if i[1] == "cd":
            if i[2] == "..":
                location.pop()
            else:
                location.append(i[2])
    else:
        if i[0] == "dir":
            main.addDirectory(location, i[1])
        else:
            main.addFile(location, i[1], i[0])

main.printDirectory()
t = main.allDirectorySizes()
minimum = 99999999
requirement = t[0] - 40000000
for i in t:
    if i >= requirement:
        if i < minimum:
            minimum = i
print(minimum)