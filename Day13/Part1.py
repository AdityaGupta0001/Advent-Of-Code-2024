# Inspiration for this logic has been taken from open source code and other solutions

import re

def parse_input(file_path):
    with open(file_path, 'r') as file:
        data = file.read()

    # Regular expression to extract information for each claw machine
    machines = []
    machine_pattern = re.compile(
        r"Button A: X\+(\d+), Y\+(\d+)\s+"
        r"Button B: X\+(\d+), Y\+(\d+)\s+"
        r"Prize: X=(\d+), Y=(\d+)"
    )

    for match in machine_pattern.finditer(data):
        Ax, Ay, Bx, By, Px, Py = map(int, match.groups())
        machines.append({'A': (Ax, Ay), 'B': (Bx, By), 'prize': (Px, Py)})

    return machines


def minimum_tokens(claw_machines):
    total_prizes = 0
    total_cost = 0

    for machine in claw_machines:
        Ax, Ay = machine['A']
        Bx, By = machine['B']
        Px, Py = machine['prize']

        min_cost = float('inf')
        found = False

        # Try all combinations of n_A and n_B
        for n_A in range(101):
            for n_B in range(101):
                if n_A * Ax + n_B * Bx == Px and n_A * Ay + n_B * By == Py:
                    cost = 3 * n_A + 1 * n_B
                    if cost < min_cost:
                        min_cost = cost
                        found = True

        if found:
            total_prizes += 1
            total_cost += min_cost

    return total_prizes, total_cost


# Input: Read from a text file
file_path = "Day13\data.txt"  # Replace with your file path
claw_machines = parse_input(file_path)

# Solve
prizes, cost = minimum_tokens(claw_machines)
print(f"Maximum prizes: {prizes}, Minimum cost: {cost}")
