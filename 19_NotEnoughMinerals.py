import math
import time
from tqdm import tqdm as tqdm #run pip3 install tqdm in terminal

start : float = time.time()
X : list = []

with open("0_Data.txt") as fileInput:
    file = list(fileInput)

linenum = 1
for line in file:
    C = line.strip()
    C = C.strip("Blueprint " + str(linenum))
    C = C.strip(": Each ore robot costs ")
    C = C.strip(" obsidian.")
    C = C.split(" ore. Each clay robot costs ")
    
    C[1] = C[1].split(" ore. Each obsidian robot costs ")
    C[1][1] = C[1][1].split(" ore and ")
    C[1][1][1] = C[1][1][1].split(" clay. Each geode robot costs ") # this is the worst parsing of all time
    linenum += 1
    X.append([[int(C[0]), 0, 0, max(int(C[1][0]), int(C[1][1][0]), int(C[1][1][1][1]))], [int(C[1][0]), 0, 0, int(C[1][1][1][0])], [int(C[1][1][0]), int(C[1][1][1][0]), 0, int(C[1][1][2])], [int(C[1][1][1][1]), 0, int(C[1][1][2]), 32]])

# print(X) # costs: [[ore cost, clay cost, obi cost, maximum amount], ...]

# interesting idea... target the next one we want to create... hmm...
# A-HA! WE CHOOSE THE ORDER WE WANT TO GET THEM IN!!!!!

# Part 1, num_days is 24

def maxoftwo(a, b):
    if a > b:
        return a
    return b

def maxoftree(a, b, c):
    return maxoftwo(maxoftwo(a, b), c)

def simpl(expr):
    if (expr > 0):
        return int(expr)
    return 0
    
def heres_the_order_of_my_list_and_its_in(next_robot, blueprint, days_left, starting_robots=[1, 0, 0, 0], starting_resources=[0, 0, 0, 0]):
    
    t = days_left
    robots = [starting_robots[0], starting_robots[1], starting_robots[2], starting_robots[3]]
    resources = [starting_resources[0], starting_resources[1], starting_resources[2], starting_resources[3]]
    
    while (t > 0 and (resources[0] < blueprint[next_robot][0] or resources[1] < blueprint[next_robot][1] or resources[2] < blueprint[next_robot][2])):
        t -= 1
        for i in range(4):
            resources[i] += robots[i]
    if (t > 0):
        t -= 1
        for i in range(4):
            resources[i] += robots[i]
        for i in range(3):
            resources[i] -= blueprint[next_robot][i]
        robots[next_robot] += 1
    boolean = False
    if (t > 0):
        boolean = True
        for i in range(4):
            if robots[i] > blueprint[i][3]:
                boolean = False
    should = [resources[3] + robots[3] * t, boolean, [t, robots, resources]] 
    
    return should
    
    ''' Failed Optimization :( Didn't make it that much slower, just didn't make it faster
    robots = [starting_robots[0], starting_robots[1], starting_robots[2], starting_robots[3]]
    resources = [starting_resources[0], starting_resources[1], starting_resources[2], starting_resources[3]]
    ndc = 100
    if next_robot < 2:
        ndc = maxoftwo(simpl((blueprint[next_robot][0] - resources[0] - 1) / robots[0] + 1) + 1, 1)
        resources[0] += ndc * robots[0] - blueprint[next_robot][0]
        resources[1] += ndc * robots[1]
        resources[2] += ndc * robots[2]
        resources[3] += ndc * robots[3]
        robots[next_robot] += 1
        # ex. if we're missing 3, then we need this many days
        # int((resources[0] - blueprint[next_robot] - 1) / robots[next_robot]) + 1 to get resources then + 1 to make robot
    elif next_robot == 2:
        if (robots[1] > 0):
            ndc = maxoftree(simpl((blueprint[2][0] - resources[0] - 1) / robots[0] + 1) + 1, simpl((blueprint[2][1] - resources[1] - 1) / robots[1] + 1) + 1, 1)
            resources[0] += ndc * robots[0] - blueprint[2][0]
            resources[1] += ndc * robots[1] - blueprint[2][1]
            resources[2] += ndc * robots[2]
            resources[3] += ndc * robots[3]
            robots[2] += 1
    else:
        if (robots[2] > 0):
            ndc = maxoftree(simpl((blueprint[3][0] - resources[0] - 1) / robots[0] + 1) + 1, simpl((blueprint[3][2] - resources[2] - 1) / robots[2] + 1) + 1, 1)
            resources[0] += ndc * robots[0] - blueprint[3][0]
            resources[1] += ndc * robots[1]
            resources[2] += ndc * robots[2] - blueprint[3][2]
            resources[3] += ndc * robots[3]
            robots[3] += 1
    
    for i in range(4):
        if robots[i] > blueprint[i][3]:
            ndc = 100
    if (ndc >= days_left):
        return [0, False, [0, 0, 0]]
    actual = [resources[3] + robots[3] * (days_left - ndc), True, [days_left - ndc, robots, resources]]
    
    return actual '''
# [number of geode, should continue branch, # days after last bot, # robots, # resources after last bot]

def iterate_bfs(current, cache, depth): # if we want to end the previous branch
    while current[depth - 1] == 3:
        depth -= 1
        current[depth] = -1
        cache[depth] = -1
    next_guess = current[depth - 1] + 1
    current[depth - 1] = -1
    cache[depth - 1] = -1
    return [depth - 1, next_guess]

def maximal_score(blueprint, num_days):
    max_score = 0
    tree = [-1] * num_days
    cachedresults = [-1] * num_days
    next_guess = 0
    
    depth = 0
    
    while (len(tree) == 0) or (tree[0] < 2): # we can never start with an obsidian
        t = 0
        if depth == 0:
            t = heres_the_order_of_my_list_and_its_in(next_guess, blueprint, num_days)
        else:
            t = heres_the_order_of_my_list_and_its_in(next_guess, blueprint, cachedresults[depth - 1][0], starting_robots=cachedresults[depth - 1][1], starting_resources=cachedresults[depth - 1][2])
        
        if t[1]: # if we go on
            if (t[0] > max_score):
                max_score = t[0]
            tree[depth] = next_guess
            cachedresults[depth] = t[2]
            next_guess = 0
            depth += 1
        else:
            if (len(tree) == 0) and (next_guess > 1):
                break
            if next_guess != 3:
                next_guess += 1
            else:
                k = iterate_bfs(tree, cachedresults, depth)
                depth = k[0]
                next_guess = k[1]
                if (depth == 0 and next_guess > 1):
                    break
    
    return max_score

c = 0
cumulative_sum = 0
for i in tqdm(X):
    c += 1
    t = maximal_score(i, 24)
    cumulative_sum += c * t

print("Part One Answer: " + str(cumulative_sum))
print("Part One Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100)) # only 12 seconds
print()

start = time.time()

cumulative_product = 1
for i in tqdm((X[0], X[1], X[2])):
    t = maximal_score(i, 32)
    cumulative_product *= t

print("Part Two Answer: " + str(cumulative_product))
print("Part Two Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100)) # around 230 seconds