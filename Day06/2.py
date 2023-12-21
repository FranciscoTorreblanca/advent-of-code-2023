import os
import math          
    
input_path = os.path.join(os.path.dirname(__file__), "input.txt")
input_file = open(input_path, "r")
file_lines = input_file.readlines()

time = 0
distance_to_beat = 0
for line in file_lines:
    data_type, data = line.split(":")
    data = int("".join(filter(bool, data.split(" "))))
    if data_type == "Time":
        time = data
    elif data_type == "Distance":
        distance_to_beat = data

inf = 0
# Not the best way to find the inf, can be better find the equation and solve
# it. The equation should to be a semi-ellipse translated time/2 to the x axis.
# So, I just iterate over possible times and find the first that is greater than
# the distance to beat.
for time_pressed in range(time):
    time_in_career = time - time_pressed
    speed = time_pressed
    distance = speed * time_in_career
    if distance > distance_to_beat:
        inf = time_pressed
        break
# Later since is simetric, we can find the last just by reflecting in the half
# of the graph.
sup = inf + ((time/2 - inf) * 2)
total_beat_combinations =  sup - inf + 1
print(total_beat_combinations)
