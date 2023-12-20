import os
import re
from collections import UserDict, UserList

class dict_range(UserDict):
    def __init__(self, ranges=None):
        self.ranges = ranges or []

    def set_range(self, source_start, dest_start, range_len):
        self.ranges.append((source_start, dest_start, range_len))

    def __getitem__(self, key):
        for source_start, dest_start, range_len in self.ranges:
            if source_start <= key < source_start + range_len:
                return dest_start + key - source_start
        return key

class list_range(UserList):
    def __init__(self, ranges=None):
        self.ranges = ranges or []
    
    def set_range(self, start, range_len):
        self.ranges.append((start, range_len))

    def __iter__ (self):
        for start, range_len in self.ranges:
            for i in range(start, start + range_len):
                yield i
    
input_path = os.path.join(os.path.dirname(__file__), "input.txt")
input_file = open(input_path, "r")
file_lines = input_file.readlines()

seeds_list = list_range()
seeds_to_soil = dict_range()
soil_to_fertilizer = dict_range()
fertilizer_to_water = dict_range()
water_to_light = dict_range()
light_to_temperature = dict_range()
temperature_to_humidity = dict_range()
humidity_to_location = dict_range()

for line in file_lines:
    if not line.strip():
        continue

    if line.startswith("seeds"):
        for match in re.finditer(r"\d+ \d+", line):
            initial_seed, seed_range = match.group().split(" ")
            seeds_list.set_range(int(initial_seed), int(seed_range))
        continue

    if line.startswith("seed"):
        mapping_dict = seeds_to_soil
        continue
    if line.startswith("soil"):
        mapping_dict = soil_to_fertilizer
        continue
    if line.startswith("fertilizer"):
        mapping_dict = fertilizer_to_water
        continue
    if line.startswith("water"):
        mapping_dict = water_to_light
        continue
    if line.startswith("light"):
        mapping_dict = light_to_temperature
        continue
    if line.startswith("temperature"):
        mapping_dict = temperature_to_humidity
        continue
    if line.startswith("humidity"):
        mapping_dict = humidity_to_location
        continue

    dest_start, source_start, range_len = line.strip().split(" ")
    mapping_dict.set_range(int(source_start), int(dest_start), int(range_len))

locations_list = []
for seed in seeds_list:
    print(seed)
    soil = seeds_to_soil[seed]
    fertilizer = soil_to_fertilizer[soil]
    water = fertilizer_to_water[fertilizer]
    light = water_to_light[water]
    temperature = light_to_temperature[light]
    humidity = temperature_to_humidity[temperature]
    location = humidity_to_location[humidity]
    locations_list.append(location)

locations_list.sort()
print(locations_list[0])