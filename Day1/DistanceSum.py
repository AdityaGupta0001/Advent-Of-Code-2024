column1 = []
column2 = []

with open('Day1\data.txt', 'r') as file:
    for line in file:
        if line.strip():
            values = line.split()
            column1.append(int(values[0]))
            column2.append(int(values[1]))

column1.sort()
column2.sort()

total_dist = 0

for i in range(len(column1)):
    total_dist+=abs(column1[i]-column2[i])

print(total_dist)


