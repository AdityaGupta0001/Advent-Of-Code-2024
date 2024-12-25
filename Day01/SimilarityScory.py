column1 = []
column2 = []

with open('Day1\data.txt', 'r') as file:
    for line in file:
        if line.strip():
            values = line.split()
            column1.append(int(values[0]))
            column2.append(int(values[1]))

similarity_score = 0


for i in column1:
    similarity_score+=i*column2.count(i)

print(similarity_score)