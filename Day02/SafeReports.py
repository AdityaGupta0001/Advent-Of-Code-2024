reports = []
with open('Day2\data.txt', 'r') as file:
    for line in file:
        if line.strip():
            values = line.split()
            for i in range(len(values)):
                values[i] = int(values[i])
            reports.append(values)

safe_count = 0
for i in reports:
    safe = True
    order = 'Increasing'
    if i[0]>i[1]:
        order = 'Decreasing'
    for j in range(len(i)-1):
        if order == 'Increasing':
            if i[j]>i[j+1] or abs(i[j]-i[j+1]) not in range(1,4):
                safe = False
                break

        if order == 'Decreasing':
            if i[j]<i[j+1] or abs(i[j]-i[j+1]) not in range(1,4):
                safe=False
                break
    if safe:
        safe_count+=1

print(safe_count)