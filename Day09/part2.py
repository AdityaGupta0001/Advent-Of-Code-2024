with open('Day9\data.txt', 'r') as f:
    input = f.read()
 
data = list(input)
 
file_system = []
free_space = False
id = 0
 
for i in data:
    if free_space:
        length = int(i)
        file_system.append((-1, int(length)))
        free_space = False
        pass
    else:
        length = int(i)
        file_system.append((id, int(length)))
        id += 1
        free_space = True
 
 
# Move blocks around
index = len(file_system) - 1
while index > 0:
    if file_system[index][0] == -1: # this is free space, do not move
        index -= 1
        continue
 
    block_length = file_system[index][1]
    # find free space to hold this block
    for j in range(0, index):
        if file_system[j][0] == -1: # found free space
            free_length = file_system[j][1]
            free_block_found = False
            if free_length == block_length: # then replace the free space with the block
                free_block_found = True
                file_system[j] = file_system[index]
            if free_length > block_length: # insert the block and reduce free space
                free_block_found = True
                file_system.insert(j, file_system[index])
                index += 1 # because we added an element
                file_system[j + 1] = (-1, free_length - block_length)
 
            if free_block_found: # then we make the old block free and exit loop
                file_system[index] = (-1, block_length)
                break
 
    # consolidate blocks of free space
    i = 0
    while i < len(file_system) - 1:
        if file_system[i][0] == -1: # free space found
            if file_system[i + 1][0] == -1: # then the next block is also free and should be combined
                file_system[i] = (-1, file_system[i + 1][1] + file_system[i][1])
                del file_system[i + 1]
        i += 1
    index -= 1
 
checksum = 0
i = 0
for f in file_system:
    if f[0] == -1:
        i += f[1]
        continue
    for _ in range(f[1]):
        checksum += i * f[0]
        i += 1
 
print(checksum)