# Inspiration for this logic has been taken from open source code and other solutions

from collections import defaultdict

# Step 1: Read input data from a text file
file_path = "Day23\data.txt"

with open(file_path, "r") as file:
    connections = [line.strip() for line in file.readlines()]

# Step 2: Build the graph as an adjacency list
graph = defaultdict(set)

for connection in connections:
    a, b = connection.split('-')
    graph[a].add(b)
    graph[b].add(a)

# Step 3: Find all sets of three interconnected computers (triangles)
triangles = set()
for node in graph:
    for neighbor1 in graph[node]:
        for neighbor2 in graph[node]:
            if neighbor1 < neighbor2 and neighbor1 in graph[neighbor2]:
                triangles.add(tuple(sorted([node, neighbor1, neighbor2])))

# Step 4: Filter triangles with at least one name starting with 't'
triangles_with_t = [
    triangle for triangle in triangles if any(computer.startswith('t') for computer in triangle)
]

# Step 5: Output the results
print(f"All triangles: {triangles}")
print(f"Triangles with at least one 't': {triangles_with_t}")
print(f"Number of triangles with at least one 't': {len(triangles_with_t)}")
