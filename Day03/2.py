import os
import re
from collections import defaultdict

input_path = os.path.join(os.path.dirname(__file__), "input.txt")
input_file = open(input_path, "r")
file_lines = input_file.readlines()

gears_positions = []
numbers_positions = []
numbers = []
for i, line in enumerate(file_lines):
    gears_iter = re.finditer('\*', line)
    if gears_iter:
        for gear in gears_iter:
            gears_positions.append((i, gear.start()))
    numbers_iter = re.finditer('\d+', line)
    if numbers_iter:
        for n in numbers_iter:
            numbers_positions.append((i, n.span()))
            numbers.append(int(n.group()))

gear_parts = defaultdict(lambda: [])
for number, (num_line, num_pos) in zip(numbers, numbers_positions):
    for gear_line, gear_pos in gears_positions:
        if gear_line in range(num_line - 1, num_line + 2):
            if gear_pos in range(num_pos[0]-1, num_pos[1]+1):
                gear_parts[(gear_line, gear_pos)].append(number)

sum = 0
for gear_numbers in gear_parts.values():
    if len(gear_numbers) == 2:
        sum += gear_numbers[0] * gear_numbers[1]

print(sum)
