from collections import deque
from pprint import pprint

def matrix_to_graph(matrix):
    rows, cols = len(matrix), len(matrix[0])
    graph = {}

    for r in range(rows):
        for c in range(cols):
            neighbors = []
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Top, Bottom, Left, Right
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    neighbors.append((nr, nc))
            graph[(r, c)] = neighbors

    return graph

def bfs(matrix, start, graph):
    """Performs BFS to count the number of 9s reachable from the start following the sequence."""
    rows, cols = len(matrix), len(matrix[0])
    queue = deque([(start, 0)])  # (current cell, current sequence number)
    visited = set()
    score = 0

    while queue:
        (r, c), seq = queue.popleft()
        
        if (r, c) in visited or matrix[r][c] != seq:
            continue
        
        visited.add((r, c))
        
        # If we've reached 9, increment the score
        if seq == 9:
            score += 1
            continue

        # Add neighbors to the queue for the next sequence number
        for nr, nc in graph[(r, c)]:
            if (nr, nc) not in visited:
                queue.append(((nr, nc), seq + 1))

    return score

def calculate_total_score(matrix):
    """Calculates the total score for all 0s in the matrix."""
    graph = matrix_to_graph(matrix)
    total_score = 0

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 0:  # Start BFS from each 0
                total_score += bfs(matrix, (r, c), graph)

    return total_score

rows = []
with open('Day10\data.txt', 'r') as file:
    for line in file:
        data = line.strip()
        rows.append(data)

matrix = []
for i in rows:
    row = []
    for j in i:
        row.append(int(j))
    matrix.append(row)

pprint(matrix)
total_score = calculate_total_score(matrix)
print("Total Score:", total_score)
