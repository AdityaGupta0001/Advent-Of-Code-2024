# import re
# string = ''
# with open('Day9\data.txt', 'r') as file:
#     string = file.read()

# data_string = ''

# ctr = 0
# for i in range(len(string)):
#     if i%2==0:
#         data_string+=str(ctr)*int(string[i])
#         ctr+=1
#     else:
#         data_string+='.'*int(string[i])

# print(data_string)
# data_list = list(data_string)

# def check_res(arr: list):
#     dot = arr.index('.')
#     val = True
#     for i in range(dot,len(arr)):
#         if arr[i] != '.':
#             val = False
#             break
#     return val

# dot_indexes = []
# for i in range(len(data_list)):
#     if data_list[i]=='.':
#         dot_indexes.append(i)

# ctr = 0
# for i in range(len(data_list)-1,-1,-1):
#     if data_list[i] in '1234567890' and check_res(data_list)==False:
#         data_list[dot_indexes[ctr]] = data_list[i]
#         data_list[i] = '.'
#         ctr+=1
# print(''.join(data_list))

# checksum = 0
# for i in range(len(data_list)):
#     if data_list[i] != '.':
#         checksum+=i*int(data_list[i])

# print(checksum)

 
 
with open('Day9\data.txt', 'r') as f:
    input = f.read()
 
data = list(input)
 
fs = []
free_space = False
id = 0
for i in data:
    if free_space:
        for _ in range(int(i)):
            fs.append(None)
        free_space = False
    else:
        for _ in range(int(i)):
             fs.append(id)
        id += 1
        free_space = True
 
#move blocks
for i in range(len(fs)-1, -1, -1):
    if fs[i] is None:
        continue
    block_id = fs[i]
    fs[i] = None
    # find free space
    for j in range(0, len(fs)):
        if fs[j] is None:
            fs[j] = block_id
            break
 
# Calculate Checksum
i = 0
checksum = 0
while fs[i] is not None:
    checksum += i * fs[i]
    i += 1
 
print(checksum)
 
 