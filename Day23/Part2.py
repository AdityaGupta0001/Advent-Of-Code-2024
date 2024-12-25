# Inspiration for this logic has been taken from open source code and other solutions

from collections import defaultdict
from itertools import combinations

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

# Step 3: Check if a set of nodes forms a clique
def is_clique(nodes):
    for a, b in combinations(nodes, 2):
        if b not in graph[a]:
            return False
    return True

# Step 4: Find the largest clique
all_nodes = list(graph.keys())
largest_clique = []

# Iterate through all subsets of nodes in descending order of size
for size in range(len(all_nodes), 0, -1):
    for subset in combinations(all_nodes, size):
        if is_clique(subset):
            largest_clique = subset
            break
    if largest_clique:
        break

# Step 5: Construct the password
password = ",".join(sorted(largest_clique))

# Output the results
print(f"Largest clique: {largest_clique}")
print(f"LAN party password: {password}")
