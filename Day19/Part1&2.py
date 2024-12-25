# Inspiration for this logic has been taken from open source code and other solutions

import time

start_time = time.time()

with open('Day19\data.txt') as file:
    towels, designs = file.read().strip().split("\n\n")

towels = set(towels.split(", "))
designs = designs.split("\n")
towel_lengths = {len(towel) for towel in towels}

def possibleDesign(target, strings, lengths):
    n = len(target)
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        for l in lengths:
            if i >= l and target[i - l:i] in strings:
                dp[i] = dp[i] or dp[i - l]
                if dp[i]:
                    break
    
    return dp[n]

def countPossible(target, strings, lengths):
    n = len(target)
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        for l in lengths:
            if i >= l and target[i - l:i] in strings:
                dp[i] += dp[i - l]
    
    return dp[n]

possible = 0
allPossible = 0

for design in designs:
    ways = countPossible(design, towels, towel_lengths)
    if ways != 0:
        possible += 1
        allPossible += ways


print("Part 1:", possible)

print("Part 2:", allPossible)

print("--- %s seconds ---" % (time.time() - start_time))