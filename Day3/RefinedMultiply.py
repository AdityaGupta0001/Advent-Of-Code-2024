import re

string = ''
with open('Day3\data.txt', 'r') as file:
    string = file.read()

def find_word_indexes(string, word):
    indexes = []
    start = 0
    while start < len(string):
        start = string.find(word, start)
        if start == -1:
            break
        indexes.append(start)
        start += len(word)
    return indexes

dos = [0]+find_word_indexes(string,'do()')
donts = find_word_indexes(string,"don't()")

check_list = dos+donts
check_list.sort()
check_list+=[len(string)-1]

d = {}
for i in dos:
    d[i] = 'do'
for i in donts:
    d[i] = 'dont'
d[len(string)-1] = 'do'
myKeys = list(d.keys())
myKeys.sort()

sd = {i: d[i] for i in myKeys}


substrings = []

for i in range(len(check_list)-1):
    if d[check_list[i]] == 'do' and d[check_list[i+1]] == 'do':
        substrings.append(string[check_list[i]:check_list[i+1]])
    elif d[check_list[i]] == 'do' and d[check_list[i+1]] == 'dont':
        substrings.append(string[check_list[i]:check_list[i+1]])


new_string = ''.join(substrings)


pattern = r'mul\(\d{1,3},\d{1,3}\)'
valid_computations =  re.findall(pattern, new_string)

computed_value = 0

for i in valid_computations:
    left_bracket = i.find("(")
    right_bracket = i.find(")")
    comma = i.find(",")

    computed_value+=int(i[left_bracket+1:comma])*int(i[comma+1:right_bracket])
print(computed_value)
