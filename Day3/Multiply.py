import re

string = ''
with open('Day3\data.txt', 'r') as file:
    string = file.read()

pattern = r'mul\(\d{1,3},\d{1,3}\)'
valid_computations =  re.findall(pattern, string)

computed_value = 0

for i in valid_computations:
    left_bracket = i.find("(")
    right_bracket = i.find(")")
    comma = i.find(",")

    computed_value+=int(i[left_bracket+1:comma])*int(i[comma+1:right_bracket])
print(computed_value)
