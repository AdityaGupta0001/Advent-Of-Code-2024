from pprint import pprint
rows = []
with open('Day6\data.txt', 'r') as file:
    for line in file:
        data = line.strip()
        rows.append(data)

matrix = []
for i in rows:
    row = []
    for j in i:
        row.append(j)
    matrix.append(row)

start_pos = []

for i in range(len(matrix)):
    if '^' in matrix[i]:
        start_pos = [i,matrix[i].index('^')]

distinct_pos_cnt = 0
current_pos = start_pos
current_direction = '^'

def check_guard_pos(pos: list, direction: str):
    border = False
    if (pos[0] == 0 and direction == '^') or (pos[1] == 0 and direction == '<') or (pos[0] == len(rows)-1 and direction == 'v') or (pos[1] == len(rows[0])-1 and direction == '>'):
        border = True
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


for i in matrix:
    for j in i:
        if j=='X':
            distinct_pos_cnt+=1

print(distinct_pos_cnt+1)