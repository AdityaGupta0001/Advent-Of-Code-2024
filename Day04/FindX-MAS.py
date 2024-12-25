from pprint import pprint
rows = []
with open('Day4\data.txt', 'r') as file:
    for line in file:
        data = line.strip()
        rows.append(data)

matrix = []
for i in rows:
    row = []
    for j in i:
        row.append(j)
    matrix.append(row)

cnt = 0

for i in range(len(rows[0])-2):
    for j in range(len(rows)-2):
        if (matrix[i][j]=='M' and matrix[i+2][j+2]=='S' and matrix[i+1][j+1]=='A' and matrix[i][j+2]=='M' and matrix[i+2][j]=='S') or (matrix[i][j]=='S' and matrix[i+2][j+2]=='M' and matrix[i+1][j+1]=='A' and matrix[i][j+2]=='S' and matrix[i+2][j]=='M') or (matrix[i][j]=='M' and matrix[i+2][j+2]=='S' and matrix[i+1][j+1]=='A' and matrix[i][j+2]=='S' and matrix[i+2][j]=='M') or (matrix[i][j]=='S' and matrix[i+2][j+2]=='M' and matrix[i+1][j+1]=='A' and matrix[i][j+2]=='M' and matrix[i+2][j]=='S'):
            cnt+=1

print(cnt)