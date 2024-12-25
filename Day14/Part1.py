# Inspiration for this logic has been taken from open source code and other solutions

import re
from dataclasses import dataclass

import numpy as np


@dataclass(slots=True)
class Robot:
    col: int
    row: int
    vcol: int
    vrow: int


def load_robots(filename):
    pattern = re.compile(r"-?\d+")
    with open(filename, "rt") as fin:
        nums = [int(m.group()) for m in re.finditer(pattern, fin.read())]
    return [Robot(*nums[i : i + 4]) for i in range(0, len(nums), 4)]


def move(robos, seconds, area_rows, area_cols):
    for r in robos:
        r.row = (r.row + r.vrow * seconds) % area_rows
        r.col = (r.col + r.vcol * seconds) % area_cols


def find_tree_second(robos, current_seconds, area_rows, area_cols):
    row_var_thres = np.var([r.row for r in robos]) * 0.5
    col_var_thres = np.var([r.col for r in robos]) * 0.5
    row_low_var, col_low_var = 0, 0

    # look for first second when variance is low (indicates clustered robots)
    while row_low_var == 0 or col_low_var == 0:
        current_seconds += 1
        move(robos, 1, area_rows, area_cols)
        if row_low_var == 0 and np.var([r.row for r in robos]) < row_var_thres:
            row_low_var = current_seconds % area_rows
        if col_low_var == 0 and np.var([r.col for r in robos]) < col_var_thres:
            col_low_var = current_seconds % area_cols

    # low row variance occurs every area_rows seconds
    # low col variance occurs every area_cols seconds
    # find second when both are low together, i.e. find x and y in this equation:
    # row_low_var + area_rows*x = col_low_var + area_cols*y

    # brute force solution
    x, y = 1, 1
    while True:
        left_side = row_low_var + area_rows * x
        right_side = col_low_var + area_cols * y
        if left_side == right_side:
            return left_side
        if left_side < right_side:
            x += 1
        else:
            y += 1


def safety_factor(robos, area_rows, area_cols):
    mid_row, mid_col = area_rows // 2, area_cols // 2
    quadrants = {(True, True): 0, (True, False): 0, (False, True): 0, (False, False): 0}

    for r in robos:
        if r.row == mid_row or r.col == mid_col:
            continue
        quadrants[r.row < mid_row, r.col < mid_col] += 1

    return (
        quadrants[True, True]
        * quadrants[True, False]
        * quadrants[False, True]
        * quadrants[False, False]
    )


def main():
    robos = load_robots("Day14\data.txt")
    area_rows, area_cols = 103, 101

    move(robos, 100, area_rows, area_cols)
    print(f"Part 1: {safety_factor(robos, area_rows, area_cols)}")
    print(f"Part 2: {find_tree_second(robos, 100, area_rows, area_cols)}")


if __name__ == "__main__":
    main()
