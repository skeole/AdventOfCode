import math
import copy

X = []

with open("0_Data.txt") as fileInput:
    file = list(fileInput)

for line in file:
    C = line.strip()
    C = C.split()
    X.append(C)

'''
Part One
A = Rock
B = Paper
C = Scissors

Same for X, Y, Z

0 for loss, 3 for draw, 6 for win
1 for rock, 2 for paper, 3 for scissors

def score(opp, you):
    oppindex = ["", "A", "B", "C"].index(opp)
    youindex = ["", "X", "Y", "Z"].index(you)
    score = youindex
    if oppindex == youindex:
        score += 3
    elif (youindex - oppindex) % 3 == 1:
        score += 6
    return score
'''

'''
Part Two
A, B, C same
X = lose
Y = draw
Z = win
'''
def score(opp, result):
    score = (["C", "A", "B"].index(opp) - ["Y", "X", "Z"].index(result) - 1) % 3 + 1
    score += ["X", "Y", "Z"].index(result) * 3
    return score


s = 0
for i in X:
    s += score(i[0], i[1])

print(s)