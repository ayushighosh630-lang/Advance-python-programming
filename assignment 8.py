
with open("input.txt", "r") as file:
    lines = file.readlines()

total_lines = len(lines)

first_two_lines = lines[:2]

with open("output.txt", "w") as file:
    file.writelines(first_two_lines)

print("Total number of lines:", total_lines)
print("First two lines are:")

for line in first_two_lines:
    print(line, end="")

print("\nFirst two lines successfully written to output.txt")