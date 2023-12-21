import os
import re
    
input_path = os.path.join(os.path.dirname(__file__), "input.txt")
input_file = open(input_path, "r")
file_lines = input_file.readlines()

# Cards ranks
HIGH_CARD = 1
ONE_PAIR = 2
TWO_PAIR = 3
THREE_OF_A_KIND = 4
FULL_HOUSE = 5
FOUR_OF_A_KIND = 6
FIVE_OF_A_KIND = 7

CARDS_VALUES = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            current_hand = array[j][1]
            next_hand = array[j + 1][1]
            for k in range(len(current_hand)):
                current_card = current_hand[k]
                next_card = next_hand[k]
                diff = CARDS_VALUES[current_card] - CARDS_VALUES[next_card]
                if diff: 
                    break
            if diff > 0:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        if already_sorted:
            break
    return array

cards = []
for line in file_lines:
    hand_cards, bid = line.split(" ")
    hand_type = HIGH_CARD
    matches = []
    for card_value in CARDS_VALUES.keys():
        matched = re.findall(card_value, hand_cards)
        if matched:
            matches.append(matched)

    pairs = 0
    has_trio = False
    for match in matches:
        if len(match) == 5:
            hand_type = FIVE_OF_A_KIND
        elif len(match) == 4:
            hand_type = FOUR_OF_A_KIND
        elif len(match) == 3:
            has_trio = True
        elif len(match) == 2:
            pairs += 1

    if has_trio and pairs == 1:
        hand_type = FULL_HOUSE
    elif has_trio:
        hand_type = THREE_OF_A_KIND
    elif pairs == 2:
        hand_type = TWO_PAIR
    elif pairs == 1:
        hand_type = ONE_PAIR

        
    cards.append((hand_type, hand_cards, int(bid)))

cards.sort(key=lambda x: x[0])
prev_card = None

sorted_cards = []
for current_card in cards:
    try:
        prev_card = sorted_cards.pop(-1)
    except IndexError:
        sorted_cards.append(current_card)
        continue
    prev_card_rank, prev_hand_cards, _ = prev_card
    current_card_rank, current_hand_cards, _ = current_card
    if prev_card_rank == current_card_rank:
        # Compare cards values
        for i, current_card_value in enumerate(current_hand_cards):
            prev_card_value = prev_hand_cards[i]
            if current_card_value != prev_card_value:
                if CARDS_VALUES[current_card_value] < CARDS_VALUES[prev_card_value]:
                    first_card = current_card
                    second_card = prev_card
                    break
                else:
                    first_card = prev_card
                    second_card = current_card
                    break
        sorted_cards.append(first_card)
        sorted_cards.append(second_card)
    else:
        sorted_cards.append(prev_card)
        sorted_cards.append(current_card)

second_sorted_cards = []
for i in range(1, FIVE_OF_A_KIND+1):
    second_sorted_cards.extend(bubble_sort(list(filter(lambda x: x[0] == i, cards))))


total = 0
for rank, card in enumerate(second_sorted_cards):
    hand_type, _, bid = card
    total += (rank+1) * bid

print(total)

