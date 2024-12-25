# Define the filename of the input text file
input_filename = "Day25\data.txt"

# Read the content of the file
with open(input_filename, "r") as file:
    example_text = file.read()

# Split the input into blocks by newlines
blocks = example_text.strip().split("\n\n")

# Separate locks and pins and calculate column lengths
locks = []
pins = []

def calculate_column_lengths(block):
    # Convert the block to a list of lines
    lines = block.strip().split("\n")
    # Calculate the number of '#' in each column
    column_lengths = [sum(1 for line in lines if line[col] == "#") - 1 for col in range(len(lines[0]))]
    return column_lengths

for block in blocks:
    lines = block.strip().split("\n")
    if "#####" in lines[0]:  # Block is a lock
        locks.append(calculate_column_lengths(block))
    elif "#####" in lines[-1]:  # Block is a pin
        pins.append(calculate_column_lengths(block))

# Print the results
print("Locks:", locks)
print("Pins:", pins)

ctr = 0

for i in range(len(locks)):
    for j in range(len(pins)):
        if locks[i][0] + pins[j][0] <= 5 and locks[i][1] + pins[j][1] <= 5 and locks[i][2] + pins[j][2] <= 5 and locks[i][3] + pins[j][3] <= 5 and locks[i][4] + pins[j][4] <= 5:
            ctr+=1

print(ctr)