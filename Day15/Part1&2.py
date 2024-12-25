# Inspiration for this logic has been taken from open source code and other solutions

import os.path
from collections import deque


DATA = os.path.join(os.path.dirname(__file__), 'day15.txt')


def __print_grid(grid):
    max_i = max(grid, key=lambda x: x[0])
    max_j = max(grid, key=lambda x: x[1])
    for i in range(max_i[0] + 1):
        line = ""
        for j in range(max_j[1] + 1):
            line += grid[(i, j)]
        print(line)


def __build_grid_and_instructions(data) -> tuple:
    grid, instructions = {}, deque()
    lines = data
    start = (-1, -1)

    for i in range(len(lines)):
        if lines[i] == "":
            for j in range(i, len(lines)):
                for c in lines[j]:
                    instructions.append(c)
            break

        for j, c in enumerate(lines[i]):
            grid[(i, j)] = c
            if c == "@":
                start = (i, j)

    return grid, instructions, start


def __modified_grid(data) -> tuple:
    lines = data.splitlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace("#", "##")
        lines[i] = lines[i].replace("O", "[]")
        lines[i] = lines[i].replace(".", "..")
        lines[i] = lines[i].replace("@", "@.")

    return __build_grid_and_instructions(lines)


def __find_boxes(grid) -> dict:
    boxes = {}
    for k, v in grid.items():
        if v == '[':
            boxes[k] = (k[0], k[1] + 1)
        elif v == ']':
            boxes[k] = (k[0], k[1] - 1)
    return boxes

def __move_robot(grid, instructions, start):
    current_position = start

    while len(instructions) != 0:
        movement = instructions.popleft()

        if movement == '^':
            dxdy = (-1, 0)
        elif movement == '>':
            dxdy = (0, 1)
        elif movement == 'v':
            dxdy = (1, 0)
        elif movement == '<':
            dxdy = (0, -1)
        else:
            raise Exception("Unknown movement")

        next_position = (current_position[0] + dxdy[0], current_position[1] + dxdy[1])

        if grid[next_position] == '#':
            continue

        if grid[next_position] == '.':
            grid[current_position] = '.'
            grid[next_position] = '@'
        elif grid[next_position] == 'O':
            next_item_position = (next_position[0] + dxdy[0], next_position[1] + dxdy[1])
            if grid[next_item_position] == '.':
                grid[next_item_position] = 'O'
                grid[next_position] = '@'
            elif grid[next_item_position] == 'O':
                pos = current_position
                shifts, space_available = 0, False

                while grid[pos] != '#':
                    if grid[pos] == '.':
                        space_available = True
                        break
                    pos = (pos[0] + dxdy[0], pos[1] + dxdy[1])
                    shifts += 1

                if not space_available:
                    continue

                # step back into last previously occupied position
                pos = (pos[0] + (-dxdy[0]), pos[1] + (-dxdy[1]))

                for _ in range(shifts):
                    val = grid[pos]
                    grid[(pos[0] + dxdy[0], pos[1] + dxdy[1])] = val
                    grid[pos] = '.'
                    pos = (pos[0] + (-dxdy[0]), pos[1] + (-dxdy[1]))
            else:
                continue

        grid[current_position] = '.'
        current_position = next_position


def __move_robot_in_second_warehouse(grid, instructions, start):
    current_position = start

    while len(instructions) != 0:
        movement = instructions.popleft()

        if movement == '^':
            dxdy = (-1, 0)
        elif movement == '>':
            dxdy = (0, 1)
        elif movement == 'v':
            dxdy = (1, 0)
        else:
            dxdy = (0, -1)

        next_position = (current_position[0] + dxdy[0], current_position[1] + dxdy[1])

        if grid[next_position] == '#':
            continue

        if grid[next_position] == '.':
            grid[current_position] = '.'
            grid[next_position] = '@'
        elif grid[next_position] == '[' or grid[next_position] == ']':
            boxes = __find_boxes(grid)
            top_points = set()
            to_move = set()
            shifts, space_available = 0, False

            positions = []
            if (grid[next_position] == '[' or grid[next_position] == ']') and (movement == '^' or movement == 'v'):
                positions.append(next_position)
                positions.append(boxes[next_position])
            else:
                positions.append(next_position)

            to_move.add(next_position)
            to_move.add(boxes[next_position])

            while len(positions) != 0:
                shifts = 0
                pp = positions.pop()
                while True:
                    if grid[pp] == '.':
                        # if we're pushing left or right,
                        # the first space we find is a
                        # viable candidate.
                        # Nice and easy!
                        if movement == '<' or movement == '>':
                            space_available = True
                            top_points.add((pp[0] + (-dxdy[0]), pp[1] + (-dxdy[1])))
                            to_move.clear()
                            positions.clear()
                            break

                        # if we're pushing up or down,
                        # we must check both halves of
                        # the box (positions list will
                        # have the positions of both
                        # halves). Additionally, we also
                        # have to check the top box(es)
                        # don't have the other half of
                        # their box hit a wall!
                        # We will do the latter here
                        second_half = boxes[(pp[0] + (-dxdy[0]), pp[1] + (-dxdy[1]))]

                        if grid[(second_half[0] + dxdy[0], second_half[1] + dxdy[1])] == '.':
                            space_available = True
                            top_points.add((pp[0] + (-dxdy[0]), pp[1] + (-dxdy[1])))
                            break
                        if grid[(second_half[0] + dxdy[0], second_half[1] + dxdy[1])] == '#':
                            space_available = False
                            break
                        if grid[(second_half[0] + dxdy[0], second_half[1] + dxdy[1])] == '[' or grid[(second_half[0] + dxdy[0], second_half[1] + dxdy[1])] == ']':
                            pp = (second_half[0] + dxdy[0], second_half[1] + dxdy[1])
                            continue
                    elif grid[pp] == '#':
                        space_available = False
                        break
                    elif grid[pp] == '[' or grid[pp] == ']':
                        if boxes[pp] not in to_move:
                            positions.append(boxes[pp])
                            to_move.add(boxes[pp])
                        to_move.add(pp)

                    pp = (pp[0] + dxdy[0], pp[1] + dxdy[1])
                    shifts += 1

                if not space_available:
                    break

            if not space_available:
                continue

            if len(to_move) != 0:
                halves = []
                for p in to_move:
                    halves.append(boxes[p])
                for a in halves:
                    to_move.add(a)

                to_move = list(to_move)
                to_move.sort(key=lambda x: (x[1], x[0]))
                if movement == 'v':
                    to_move.reverse()

                for p in to_move:
                    grid[(p[0] + dxdy[0], p[1])] = grid[p]
                    grid[p] = '.'
            else:
                for p in top_points:
                    for _ in range(shifts):
                        val = grid[p]
                        grid[(p[0] + dxdy[0], p[1] + dxdy[1])] = val
                        grid[p] = '.'
                        p = (p[0] + (-dxdy[0]), p[1] + (-dxdy[1]))
        else:
            continue

        grid[current_position] = '.'
        grid[next_position] = '@'
        current_position = next_position

def part_one(data) -> int:
    grid, instructions, start = __build_grid_and_instructions(data.splitlines())
    __move_robot(grid, instructions, start)
    result = 0
    for k, v in grid.items():
        if v == 'O':
            result += ((100 * k[0]) + k[1])
    return result


def part_two(data) -> int:
    grid, instructions, start = __modified_grid(data)
    __move_robot_in_second_warehouse(grid, instructions, start)
    result = 0
    for k, v in grid.items():
        if v == '[':
            result += ((100 * k[0]) + k[1])
    return result

def main() -> int:
    with open('Day15\data.txt','r') as f:
        data = f.read()
        print("Part 1: " + str(part_one(data)))
        print("Part 2: " + str(part_two(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())