#!/usr/bin/env python3

from collections import defaultdict

def process_input(filename):
    """Acquire input data"""
    with open(filename) as file:
        input = file.read().splitlines()

    stones = defaultdict(int)
    for stone in input[0].split():
        stone = int(stone)
        stones[stone] += 1

    return stones


def blink_times(blinks):
    for i in range(blinks):
        blink()
        print(i,len(stones))
    return 


def blink():
    stonework = dict(stones)
    for stone, count in stonework.items():
        if count == 0: continue
        if stone == 0:
            stones[1] += count
            stones[0] -= count
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            new_len = int(len(stone_str) / 2)
            stone_1 = int(stone_str[:new_len])
            stone_2 = int(stone_str[new_len:])
            stones[stone_1] += count
            stones[stone_2] += count
            stones[stone] -= count
        else:
            stones[stone * 2024] += count
            stones[stone] -= count
    return

filename = 'Day11\data.txt'

stones = process_input(filename)

blink_times(75)

print()
print('Stones =', sum(stones.values()))
