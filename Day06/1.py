import os
    
input_path = os.path.join(os.path.dirname(__file__), "input.txt")
input_file = open(input_path, "r")
file_lines = input_file.readlines()

times = []
distances_to_beat = []
for line in file_lines:
    data_type, data = line.split(":")
    data = [int(x) for x in filter(bool, data.split(" "))]
    if data_type == "Time":
        times = data
    elif data_type == "Distance":
        distances_to_beat = data


print(times, distances_to_beat)
result = 1
for time, distance_to_beat in zip(times, distances_to_beat):
    total_beat_combinations = 0
    for time_pressed in range(time + 1):
        time_in_career = time - time_pressed
        speed = time_pressed
        distance = speed * time_in_career
        if distance > distance_to_beat:
            total_beat_combinations += 1
    if total_beat_combinations:
        result *= total_beat_combinations

print(result)