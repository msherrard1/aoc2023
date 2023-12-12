from datetime import datetime
startTime = datetime.now()
from itertools import chain

DESTINATION_RANGE_START_POS = 0
SOURCE_RANGE_START_POS = 1
RANGE_LENGTH_POS = 2

def grouped(iterable, n):
    return zip(*[iter(iterable)]*n)

def parse(input_data):
    lines = input_data.splitlines()

    almanac = {}
    current_map_key = None

    # break input in seeds line and map lines

    for line_number, line in enumerate(lines):
        split_line = line.split()
        if len(split_line) == 0 and current_map_key == None:
            pass
        elif len(split_line) == 0:
            almanac[current_map_key] = current_map_entries
            current_map_key = None
            current_map_entries = None
        elif split_line[0] == 'seeds:':
            seed_ranges = []
            for start, end in grouped(split_line[1:],2):
                seed_ranges.append((int(start),int(end)))
            almanac['seeds'] = seed_ranges
        elif split_line[-1] == "map:":
            map_name = split_line[0]
            current_map_key = (map_name.split('-')[0],map_name.split('-')[2])
            current_map_entries = []
        else:
            values = tuple([int(x) for x in split_line])
            current_map_entries.append(values)

    if current_map_key != None:
        almanac[current_map_key] = current_map_entries

    return almanac

def resolve(source_value, source_category, almanac):

    category_map = None
    for key in almanac.keys():
        if key[0] == source_category:
            category_map = key
            target_category = key[1]
    
    if category_map == None:
        return source_value

    for map_entry in almanac[category_map]:
        source_range_start = map_entry[SOURCE_RANGE_START_POS]
        range_length = map_entry[RANGE_LENGTH_POS]
        if value in range(source_range_start,source_range_start+range_length):
            distance_from_start = source_value - source_range_start
            destination_range_start = map_entry[DESTINATION_RANGE_START_POS]
            destination_range_end = destination_range_start + range_length
            destination_value = destination_range_start + distance_from_start
            local_skippable = destination_range_end - destination_value

            return resolve(destination_value, target_category, almanac)
    
    return resolve(value, target_category, almanac)

def resolve_up(value, target_category, almanac):

    category_map = None
    for key in almanac.keys():
        if key[1] == target_category:
            category_map = key
            source_category = key[0]
    
    if category_map == None:
        return value

    for map_entry in almanac[category_map]:
        destination_range_start = map_entry[DESTINATION_RANGE_START_POS]
        range_lenth = map_entry[RANGE_LENGTH_POS]

        if value in range(destination_range_start,destination_range_start + range_lenth):
            distance_from_start = value - destination_range_start
            source_range_start = map_entry[SOURCE_RANGE_START_POS]
            return resolve_up(source_range_start + distance_from_start, source_category, almanac)

    return resolve_up(value, source_category, almanac)

# def get_lowest_location(almanac):

#     lowest_location = None

#     seeds = []

#     for seed_range in almanac['seeds']:
#         start_seed_range = seed_range[0]
#         seed_range_length = seed_range[1]
#         for i in range(start_seed_range,start_seed_range+seed_range_length):
#             seeds.append(i)

#     print("seeds generated")

#     for seed in seeds:
#         location = resolve(seed, 'seed', almanac) 
#         if lowest_location == None or location < lowest_location:
#             lowest_location = location

#     return lowest_location        

# def get_lowest_location(almanac):

#     seed_ranges = []
#     for seed_pair_entry in almanac["seeds"]:
#         seed_range = range(seed_pair_entry[0],seed_pair_entry[0]+seed_pair_entry[1])
#         seed_ranges.append(seed_range)

#     next_location = 1094349260

#     while next_location > 0:
#         seed = resolve_up(next_location, "location", almanac)

#         for seed_range in seed_ranges:
#             if seed in seed_range:
#                 print(next_location)

#         next_location -= 1

    # almanac[('humidity','location')].sort(key=lambda x: x[0])

    # for map_entry in almanac[('humidity','location')]:
    #     destination_range_start = map_entry[DESTINATION_RANGE_START_POS]
    #     destination_range_end = destination_range_start + map_entry[RANGE_LENGTH_POS]

    #     print(destination_range_start)

    #     for location_value in range(destination_range_start,destination_range_end):
    #         print(location_value)
    #         # if resolve_up(location_value, "location", almanac) != False:
    #         #     return location_value

def resolve_skippable(source_value, source_category, max_skippable, almanac):
    category_map = None
    for key in almanac.keys():
        if key[0] == source_category:
            category_map = key
            target_category = key[1]
    
    if category_map == None:
        return (source_value, max_skippable)

    for map_entry in almanac[category_map]:
        source_range_start = map_entry[SOURCE_RANGE_START_POS]
        range_length = map_entry[RANGE_LENGTH_POS]
        if source_value in range(source_range_start,source_range_start+range_length):
            distance_from_start = source_value - source_range_start
            destination_range_start = map_entry[DESTINATION_RANGE_START_POS]
            destination_range_end = destination_range_start + range_length
            destination_value = destination_range_start + distance_from_start
            local_skippable = destination_range_end - destination_value

            return resolve_skippable(destination_value, target_category, min(max_skippable,local_skippable), almanac)
    
    return resolve_skippable(source_value, target_category, max_skippable, almanac)

def get_lowest_location(almanac):

    lowest_location = None

    for seed_range in almanac['seeds']:

        next_seed = seed_range[0]
        max_skippable = seed_range[1]
        
        while next_seed < seed_range[0] + seed_range[1]:
            result = resolve_skippable(next_seed, 'seed', max_skippable, almanac)
            location_found = result[0]

            if lowest_location == None or location_found < lowest_location:
                lowest_location = location_found

            next_seed += result[1]
    
    return lowest_location

if __name__ == "__main__":
    with open('5input.txt', 'r') as f:
        input_data = f.read()

#     input_data = """seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4

#     """

    almanac = parse(input_data)

    # for key, entry in almanac.items():
    #     print(key)
    #     print(entry)

    print(get_lowest_location(almanac))
    # print(resolve(82,'seed',almanac))
    print(datetime.now() - startTime)