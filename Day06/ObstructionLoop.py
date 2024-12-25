from pprint import pprint
from copy import deepcopy
rows = []
with open('Day6\data.txt', 'r') as file:
    for line in file:
        data = line.strip()
        rows.append(data)

matrix = []
matrix_2 = []
for i in range(len(rows)):
    row = []
    for j in range(len(rows[i])):
        row.append(rows[i][j])
    matrix.append(row)

matrix_2 = deepcopy(matrix)

start_pos = []

for i in range(len(matrix)):
    if '^' in matrix[i]:
        start_pos = [i,matrix[i].index('^')]

obstruction_cnt = 0
current_pos = start_pos
current_pos_copy = start_pos.copy()
current_direction = '^'

def check_guard_pos(pos: list, direction: str):
    border = False
    if (pos[0] == 0 and direction == '^') or (pos[1] == 0 and direction == '<') or (pos[0] == len(rows)-1 and direction == 'v') or (pos[1] == len(rows[0])-1 and direction == '>'):
        border = True
        matrix[pos[0]][pos[1]] = 'X'
    return border

def turn_90(direction: str):
    directions = ['^','>','v','<']
    current_direction = directions.index(direction)
    next_direction = directions[(current_direction+1)%4]
    return next_direction

while check_guard_pos(current_pos, current_direction) == False:
    if current_direction=='^':
        if matrix[current_pos[0]-1][current_pos[1]] in ['.','X']:
            matrix[current_pos[0]][current_pos[1]] = 'X'
            matrix[current_pos[0]-1][current_pos[1]] = '^'
            current_pos[0]-=1
        elif matrix[current_pos[0]-1][current_pos[1]] == '#':
            current_direction = turn_90(current_direction)
    elif current_direction=='>':
        if matrix[current_pos[0]][current_pos[1]+1] in ['.','X']:
            matrix[current_pos[0]][current_pos[1]] = 'X'
            matrix[current_pos[0]][current_pos[1]+1] = '>'
            current_pos[1]+=1
        elif matrix[current_pos[0]][current_pos[1]+1] == '#':
            current_direction = turn_90(current_direction)
    elif current_direction=='v':
        if matrix[current_pos[0]+1][current_pos[1]] in ['.','X']:
            matrix[current_pos[0]][current_pos[1]] = 'X'
            matrix[current_pos[0]+1][current_pos[1]] = 'v'
            current_pos[0]+=1
        elif matrix[current_pos[0]+1][current_pos[1]] == '#':
            current_direction = turn_90(current_direction)
    elif current_direction=='<':
        if matrix[current_pos[0]][current_pos[1]-1] in ['.','X']:
            matrix[current_pos[0]][current_pos[1]] = 'X'
            matrix[current_pos[0]][current_pos[1]-1] = '<'
            current_pos[1]-=1
        elif matrix[current_pos[0]][current_pos[1]-1] == '#':
            current_direction = turn_90(current_direction)

visited_positions = []
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j]=='X':
            visited_positions.append([i,j])

for i in visited_positions:
    temp_matrix = deepcopy(matrix_2)
    temp_matrix[i[0]][i[1]] = 'O'
    ctr = len(temp_matrix)*len(temp_matrix[0])
    current_pos_2 = current_pos_copy.copy()
    current_direction_2 = '^'
    while check_guard_pos(current_pos_2, current_direction_2) == False:
        if current_direction_2=='^':
            if temp_matrix[current_pos_2[0]-1][current_pos_2[1]] in ['.','X']:
                temp_matrix[current_pos_2[0]][current_pos_2[1]] = 'X'
                temp_matrix[current_pos_2[0]-1][current_pos_2[1]] = '^'
                current_pos_2[0]-=1
                ctr-=1
            elif temp_matrix[current_pos_2[0]-1][current_pos_2[1]] in ['#','O']:
                current_direction_2 = turn_90(current_direction_2)
        elif current_direction_2=='>':
            if temp_matrix[current_pos_2[0]][current_pos_2[1]+1] in ['.','X']:
                temp_matrix[current_pos_2[0]][current_pos_2[1]] = 'X'
                temp_matrix[current_pos_2[0]][current_pos_2[1]+1] = '>'
                current_pos_2[1]+=1
                ctr-=1
            elif temp_matrix[current_pos_2[0]][current_pos_2[1]+1] in ['#','O']:
                current_direction_2 = turn_90(current_direction_2)
        elif current_direction_2=='v':
            if temp_matrix[current_pos_2[0]+1][current_pos_2[1]] in ['.','X']:
                temp_matrix[current_pos_2[0]][current_pos_2[1]] = 'X'
                temp_matrix[current_pos_2[0]+1][current_pos_2[1]] = 'v'
                current_pos_2[0]+=1
                ctr-=1
            elif temp_matrix[current_pos_2[0]+1][current_pos_2[1]] in ['#','O']:
                current_direction_2 = turn_90(current_direction_2)
        elif current_direction_2=='<':
            if temp_matrix[current_pos_2[0]][current_pos_2[1]-1] in ['.','X']:
                temp_matrix[current_pos_2[0]][current_pos_2[1]] = 'X'
                temp_matrix[current_pos_2[0]][current_pos_2[1]-1] = '<'
                current_pos_2[1]-=1
                ctr-=1
            elif temp_matrix[current_pos_2[0]][current_pos_2[1]-1] in ['#','O']:
                current_direction_2 = turn_90(current_direction_2)
        
        if ctr<0:
            obstruction_cnt+=1
            break

print(obstruction_cnt)