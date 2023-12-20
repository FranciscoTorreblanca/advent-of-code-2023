import os
from collections import UserDict

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
    
input_path = os.path.join(os.path.dirname(__file__), "input.txt")
input_file = open(input_path, "r")
file_lines = input_file.readlines()

seeds_list = []
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
        _, seeds = line.split(":")
        seeds_list = (seeds.strip().split(" "))
        seeds_list = [int(x) for x in seeds_list]
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