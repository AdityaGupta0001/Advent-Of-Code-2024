from pprint import pprint
rows = []
with open('Day4\data.txt', 'r') as file:
    for line in file:
        data = line.strip()
        rows.append(data)

columns = []
for i in range(len(rows[0])):
    columns.append('')
for i in range(len(columns)):
    for j in range(len(rows[0])):
        columns[i]+=rows[j][i]

matrix = []
for i in rows:
    row = []
    for j in i:
        row.append(j)
    matrix.append(row)

rev_matrix = []
for i in rows:
    row = []
    for j in range(len(i)-1,-1,-1):
        row.append(i[j])
    rev_matrix.append(row)

diagonals = []
for i in range(len(rows)+len(columns)-1):
    diagonals.append('')
for i in range(len(rows[0])):
    for j in range(len(columns[0])):
        diagonals[i+j]+=matrix[i][j]

rev_diagonals = []
for i in range(len(rows)+len(columns)-1):
    rev_diagonals.append('')
for i in range(len(rows[0])):
    for j in range(len(columns[0])):
        rev_diagonals[i+j]+=rev_matrix[i][j]

total_count = 0
row_cnt = 0
col_cnt = 0
diag=0
revdiag = 0

for i in rows:
    row_cnt+=i.count('XMAS')+i.count('SAMX')

for i in columns:
    col_cnt+=i.count('XMAS')+i.count('SAMX')

for i in diagonals:
    diag+=i.count('XMAS')+i.count('SAMX')

for i in rev_diagonals:
    revdiag+=i.count('XMAS')+i.count('SAMX')

total_count = row_cnt+col_cnt+diag+revdiag

print(total_count)
