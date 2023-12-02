import os
import re

input_path = os.path.join(os.path.dirname(__file__), "input.txt")
input_file = open(input_path, "r")
file_lines = input_file.readlines()

r_cubes = 12
g_cubes = 13
b_cubes = 14

re_pattern = r"\d+ (red|green|blue)"

game_power_sets_sum = 0
for game in file_lines:
    game_id = game.split(" ")[1][:-1]
    matches = [m.group() for m in re.finditer(re_pattern, game)]
    min_r_cubes = 0
    min_g_cubes = 0
    min_b_cubes = 0
    for match in matches:
        (n, color) = match.split(" ")
        if color == "red" and int(n) > min_r_cubes:
            min_r_cubes = int(n)
        elif color == "green" and int(n) > min_g_cubes:
            min_g_cubes = int(n)
        elif color == "blue" and int(n) > min_b_cubes:
            min_b_cubes = int(n)

    game_set_power = min_r_cubes * min_g_cubes * min_b_cubes
    game_power_sets_sum += game_set_power

print("Sum of the power games:", game_power_sets_sum)
