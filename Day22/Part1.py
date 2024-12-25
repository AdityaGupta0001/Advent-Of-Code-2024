import math

secret_nums = []
with open('Day22\data.txt', 'r') as file:
    for line in file:
        if line.strip():
            secret_nums.append(int(line))

def mix(num1: int, num2: int):
    return num1^num2

def prune(num: int):
    return num%16777216

def produce_secret_num(num: int, nth_pos: int):
    start = num
    for i in range(nth_pos):
        start = prune(mix(start,start*64))
        start = prune(mix(start,math.floor(start/32)))
        start = prune(mix(start*2048,start))
    return start

res = 0

for j in secret_nums:
    res+=produce_secret_num(j,2000)

print(res)