from pprint import pprint
reports = []
with open('Day2\data.txt', 'r') as file:
    for line in file:
        if line.strip():
            values = line.split()
            for i in range(len(values)):
                values[i] = int(values[i])
            reports.append(values)

def isSafe(arr):
    safe = True
    order = 'Increasing'
    if arr[0]>arr[1]:
        order = 'Decreasing'
    for i in range(len(arr)-1):
        if order == 'Increasing':
            if arr[i]>arr[i+1] or abs(arr[i]-arr[i+1]) not in range(1,4):
                safe = False
                break
        if order == 'Decreasing':
            if arr[i]<arr[i+1] or abs(arr[i]-arr[i+1]) not in range(1,4):
                safe=False
                break
    return safe

safe_count = 0
saferep = []
for i in reports:
    safe = isSafe(i)
    if safe:
        safe_count+=1
        saferep.append(i)
    else:
        level_reduced_reports = []
        for j in range(len(i)):
            temp = i.copy()
            temp.pop(j)
            level_reduced_reports.append(temp)

        print(level_reduced_reports)
        for k in level_reduced_reports:
            if isSafe(k):
                safe_count+=1
                saferep.append(i)
                break

print(safe_count)