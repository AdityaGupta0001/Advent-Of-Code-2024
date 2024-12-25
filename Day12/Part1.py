from collections import deque

# Inspiration for this logic has been taken from open source code and other solutions

def calculate_fencing_price(map_data):
    rows = len(map_data)
    cols = len(map_data[0])
    visited = [[False] * cols for _ in range(rows)]

    def is_valid(x, y, char):
        return 0 <= x < rows and 0 <= y < cols and map_data[x][y] == char and not visited[x][y]

    def flood_fill(x, y):
        queue = deque([(x, y)])
        visited[x][y] = True
        region_cells = []
        perimeter = 0
        
        while queue:
            cx, cy = queue.popleft()
            region_cells.append((cx, cy))
            # Check all 4 directions
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if is_valid(nx, ny, map_data[cx][cy]):
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                elif not (0 <= nx < rows and 0 <= ny < cols) or map_data[nx][ny] != map_data[cx][cy]:
                    perimeter += 1  # Edge contributes to perimeter

        area = len(region_cells)
        return area, perimeter

    total_price = 0

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                area, perimeter = flood_fill(i, j)
                total_price += area * perimeter

    return total_price

def read_map_from_file(filename):
    with open(filename, 'r') as file:
        map_data = [list(line.strip()) for line in file]
    return map_data

# Example Usage
filename = "Day12\data.txt"  # Replace with the path to your input file
map_data = read_map_from_file(filename)
total_price = calculate_fencing_price(map_data)
print(f"Total price for fencing all regions: {total_price}")
