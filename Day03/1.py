import os
import re

input_path = os.path.join(os.path.dirname(__file__), "input.txt")
input_file = open(input_path, "r")
file_lines = input_file.readlines()

symbols_positions = []
numbers_positions = []
numbers = []
for i, line in enumerate(file_lines):
    symbols_iter = re.finditer('(?!\d|\.).', line)
    if symbols_iter:
        for s in symbols_iter:
            symbols_positions.append((i, s.start()))
    numbers_iter = re.finditer('\d+', line)
    if numbers_iter:
        for n in numbers_iter:
            numbers_positions.append((i, n.span()))
            numbers.append(int(n.group()))

sum = 0
for number, (num_line, num_pos) in zip(numbers, numbers_positions):
    for sym_line, sym_pos in symbols_positions:
        if sym_line in range(num_line - 1, num_line + 2):
            if sym_pos in range(num_pos[0]-1, num_pos[1]+1):
                sum += number
                break

print(sum)
