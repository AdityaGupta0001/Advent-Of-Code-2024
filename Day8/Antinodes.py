# from pprint import pprint
# from copy import deepcopy
# rows = []
# with open('Day8\data.txt', 'r') as file:
#     for line in file:
#         data = line.strip()
#         rows.append(data)

# matrix = []

# for i in rows:
#     row = []
#     for j in i:
#         row.append(j)
#     matrix.append(row)

# anntinode_makers = []

# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         for k in range(i+1,len(matrix)):
#             if matrix[i][j] in matrix[k] and matrix[i][j] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890':
#                 anntinode_makers.append([[i,j],[k,matrix[k].index(matrix[i][j])]])

# # pprint(matrix)
# # print() 
# # print(anntinode_makers)

# for i in range(len(anntinode_makers)):
#     pair = anntinode_makers[i]
#     row_diff = abs(anntinode_makers[i][0][0] - anntinode_makers[i][1][0])
#     col_diff = abs(anntinode_makers[i][0][1] - anntinode_makers[i][1][1])

#     if pair[0][0]<pair[1][0] and pair[0][1]>pair[1][1]:
#         if pair[0][0]-row_diff in range(0,len(matrix)) and pair[0][1]+col_diff in range(0,len(matrix[0])):
#             if matrix[pair[0][0]-row_diff][pair[0][1]+col_diff] == '.':
#                 matrix[pair[0][0]-row_diff][pair[0][1]+col_diff] = '#'
#         if pair[1][0]+row_diff in range(0,len(matrix)) and pair[1][1]-col_diff in range(0,len(matrix[0])):
#             if matrix[pair[1][0]+row_diff][pair[1][1]-col_diff] == '.':
#                 matrix[pair[1][0]+row_diff][pair[1][1]-col_diff] = '#'
#     elif pair[0][0]<pair[1][0] and pair[0][1]<pair[1][1]:
#         if pair[0][0]-row_diff in range(0,len(matrix)) and pair[0][1]-col_diff in range(0,len(matrix[0])):
#             if matrix[pair[0][0]-row_diff][pair[0][1]-col_diff] == '.':
#                 matrix[pair[0][0]-row_diff][pair[0][1]-col_diff] = '#'
#         if pair[1][0]+row_diff in range(0,len(matrix)) and pair[1][1]+col_diff in range(0,len(matrix[0])):
#             if matrix[pair[1][0]+row_diff][pair[1][1]+col_diff] == '.':
#                 matrix[pair[1][0]+row_diff][pair[1][1]+col_diff] = '#'

# total_antinodes = 0

# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if matrix[i][j] == '#':
#             total_antinodes+=1

# print(total_antinodes+1)

def get_grid(filename):
    with open(filename) as f:
        grid = f.read().splitlines()
        bounds = len(grid[0]) + len(grid) * 1j
        return grid, bounds

def find_in_grid(grid, c):
    idx = []
    y = 1
    for line in grid:
        l = list(line)
        for x in range(len(l)):
            if l[x] == c:
                idx.append(x + 1 + y * 1j)
        y += 1
    return idx

grid, bounds = get_grid("Day8\data.txt")
antenas = set(i for i in "".join(grid))
antenas.remove(".")

res1 = set()
res2 = set()
for a in antenas:
    idx = find_in_grid(grid,a)
    for i1 in idx:
        for i2 in idx:
            if i1!=i2 and 0<(vec:=2*i1-i2).real<=bounds.real and 0<vec.imag<=bounds.imag : res1.add(vec)
            temp = i1  
            if (vec:=i1-i2) != 0j:
                while 0<temp.real<=bounds.real and 0<temp.imag<=bounds.imag:
                    res2.add(temp)
                    temp+=vec
print(len(res1))
print(len(res2))