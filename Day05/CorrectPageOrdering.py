from pprint import pprint
data = []
rules = []
updates = []
partition = False
with open('Day5\data.txt', 'r') as file:
    for line in file:
        if line=='\n':
            partition=True
            continue
        
        if partition==False:
            rule = line.rstrip('\n').split('|')
            rules.append((rule[0],rule[1]))
        
        else:
            update = line.rstrip('\n').split(',')
            updates.append(update)


def checkByRule(arr: list):
    new_arr = arr.copy()
    for n in range(len(new_arr) - 1, 0, -1):
        swapped = False  
        for i in range(n):
            if (new_arr[i+1],new_arr[i]) in rules:
                new_arr[i], new_arr[i + 1] = new_arr[i + 1], new_arr[i]
                swapped = True
        if not swapped:
            break
    return new_arr

def findMiddleElement(arr: list):
    if len(arr)%2!=0:
        return int((len(arr)+1)/2)
    else:
        return int(len(arr)/2)

result = 0
for i in range(len(updates)):
    change = checkByRule(updates[i])
    if change==updates[i]:
        result+=int(updates[i][findMiddleElement(updates[i])-1])

print(result)