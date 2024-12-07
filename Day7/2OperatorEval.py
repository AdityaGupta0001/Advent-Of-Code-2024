from itertools import product

def generate_permutations(n):
    permutations = list(product(['*', '+'], repeat=n))
    return [''.join(p) for p in permutations]

equations = []
with open('Day7\data.txt', 'r') as file:
    for line in file:
        temp = []
        if line.strip():
            values = line.split()
            temp.append(values[0][0:len(values[0])-1])
            temp.extend(values[1::])
            equations.append(temp)

result = 0

for i in range(len(equations)):
    valid_check = False
    res = int(equations[i][0])
    permutations = generate_permutations(len(equations[i])-2)
    for j in range(len(permutations)):
        calculate = str((len(equations[i])-1)*'(')
        for k in range(1,len(equations[i])-1):  
            calculate+=equations[i][k]+')'+permutations[j][k-1]
        calculate+=equations[i][-1]+')'
        if eval(calculate)==res:
            valid_check = True
            break
    if valid_check:
        result+=res
print(result)
