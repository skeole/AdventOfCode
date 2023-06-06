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

print("Part One Answer: " + str("part one answer"))
print("Part One Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))
start = time.time()
print()

print("Part Two Answer: " + str("part two answer"))
print("Part Two Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))