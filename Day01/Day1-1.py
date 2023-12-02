import os

input_path = os.path.join(os.path.dirname(__file__), "input.txt")
input_file = open(input_path, "r")
file_lines = input_file.readlines()
result = 0

for line in file_lines:
    digits = [c for c in line if c.isdigit()]
    result = result + int(digits[0] + digits[-1])

print(result)
