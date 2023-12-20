import os
import re
from collections import defaultdict

input_path = os.path.join(os.path.dirname(__file__), "input.txt")
input_file = open(input_path, "r")
file_lines = input_file.readlines()

copy_cards = defaultdict(int)
total_cards = 0
for line in file_lines:
    current_card_number = int(re.search(r"\d+", line).group())
    total_cards += 1 + copy_cards[current_card_number]
    (winning_numbers, numbers) = line.split(":")[1].split("|")
    winning_numbers = list(filter(bool,winning_numbers.strip().split(" ")))
    numbers = list(filter(bool, numbers.strip().split(" ")))

    card_matches = 0
    for number in numbers:
        if number in winning_numbers:
            card_matches += 1
    if card_matches:
        for i in range(current_card_number+1, current_card_number+card_matches+1):
            copy_cards[i] += 1 + copy_cards[current_card_number]

print(total_cards)