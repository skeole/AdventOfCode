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
    X.append(int(C))

# X is literally our data
Grove_Data = deepcopy(X) # this is the order of the list and it's in