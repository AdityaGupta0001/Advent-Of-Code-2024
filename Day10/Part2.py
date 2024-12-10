from collections import deque

def matrix_to_graph(matrix):
    """Converts the matrix into a graph representation where each cell points to its neighbors."""
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

def count_distinct_paths(matrix, start, graph):
    """Counts the number of distinct hiking trails from a trailhead."""
    rows, cols = len(matrix), len(matrix[0])
    queue = deque([(start, 0)])  # (current cell, current sequence number)
    path_counts = {}  # Stores the number of paths to each (cell, sequence)

    while queue:
        (r, c), seq = queue.popleft()

        # Skip if the cell does not match the current sequence
        if matrix[r][c] != seq:
            continue

        # If this (cell, sequence) has been visited, update the path count
        if (r, c, seq) not in path_counts:
            path_counts[(r, c, seq)] = 0
        path_counts[(r, c, seq)] += 1

        # Add neighbors to the queue for the next sequence
        for nr, nc in graph[(r, c)]:
            if matrix[nr][nc] == seq + 1:
                queue.append(((nr, nc), seq + 1))

    # Sum paths reaching all cells with value 9
    return sum(path_counts[(r, c, 9)] for r, c, seq in path_counts if seq == 9)

def calculate_total_rating(matrix):
    """Calculates the total trailhead ratings for all 0s in the matrix."""
    graph = matrix_to_graph(matrix)
    total_rating = 0

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 0:  # Start counting from each trailhead
                total_rating += count_distinct_paths(matrix, (r, c), graph)

    return total_rating

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

total_score = calculate_total_rating(matrix)
print("Total Score:", total_score)
