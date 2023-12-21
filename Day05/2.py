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
        for match in re.finditer(r"\d+ \d+", line):
            initial_seed, seed_range = match.group().split(" ")
            seeds_list.append((int(initial_seed), int(seed_range)))
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

def complete_ranges(target_mapping):
    target_mapping.ranges.sort(key=lambda x: x[0])
    start = 0
    for target_dest_start, _, target_range_len in target_mapping.ranges:
        if target_dest_start > start:
            target_mapping.ranges.append((start, start, target_dest_start - start))
        start = target_dest_start + target_range_len
    target_mapping.ranges.sort(key=lambda x: x[0])

complete_ranges(seeds_to_soil)
complete_ranges(soil_to_fertilizer)
complete_ranges(fertilizer_to_water)
complete_ranges(water_to_light)
complete_ranges(light_to_temperature)
complete_ranges(temperature_to_humidity)
complete_ranges(humidity_to_location)

def inverse_mapping(original_mapping):
    inversed_mapping = dict_range()
    for dest_start, source_start, range_len in original_mapping.ranges:
        inversed_mapping.set_range(source_start, dest_start, range_len)
    # Sort by source start
    inversed_mapping.ranges.sort(key=lambda x: x[1])
    return inversed_mapping

soil_to_seeds = inverse_mapping(seeds_to_soil)
fertilizer_to_soil = inverse_mapping(soil_to_fertilizer)
water_to_fertilizer = inverse_mapping(fertilizer_to_water)
light_to_water = inverse_mapping(water_to_light)
temperature_to_light = inverse_mapping(light_to_temperature)
humidity_to_temperature = inverse_mapping(temperature_to_humidity)
location_to_humidity = inverse_mapping(humidity_to_location)

end_loop = False
# It works after some time, but not in an efficient way heheh
for location_start, humidity_start, range_len in humidity_to_location.ranges:
    for location in range(location_start, location_start + range_len):
        humidity = location_to_humidity[location]
        temperature = humidity_to_temperature[humidity]
        light = temperature_to_light[temperature]
        water = light_to_water[light]
        fertilizer = water_to_fertilizer[water]
        soil = fertilizer_to_soil[fertilizer]
        seed = soil_to_seeds[soil]
        for seed_start, seed_range in seeds_list:
            if seed_start <= seed < seed_start + seed_range:
                print("seed:", seed)
                print("location:", location)
                end_loop = True
                break
        if end_loop:
            break
    if end_loop:
        break
