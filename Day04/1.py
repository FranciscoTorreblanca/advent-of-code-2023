import os

input_path = os.path.join(os.path.dirname(__file__), "input.txt")
input_file = open(input_path, "r")
file_lines = input_file.readlines()

cards_worth = 0
for line in file_lines:
    (winning_numbers, numbers) = line.split(":")[1].split("|")
    winning_numbers = list(filter(bool,winning_numbers.strip().split(" ")))
    numbers = list(filter(bool, numbers.strip().split(" ")))
    matches = 0
    for number in numbers:
        if number in winning_numbers:
            matches += 1
    if matches:
        cards_worth += 2**(matches - 1)

print(cards_worth)
