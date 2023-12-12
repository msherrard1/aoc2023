from datetime import datetime
startTime = datetime.now()

DESTINATION_RANGE_START_POS = 0
SOURCE_RANGE_START_POS = 1
RANGE_LENGTH_POS = 2

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
            almanac['seeds'] = [int(x) for x in split_line[1:]]
        elif split_line[-1] == "map:":
            map_name = split_line[0]
            current_map_key = (map_name.split('-')[0],map_name.split('-')[2])
            current_map_entries = []
        else:
            values = tuple([int(x) for x in split_line])
            current_map_entries.append(values)

    return almanac

def resolve(value, source_category, almanac):

    category_map = None
    for key in almanac.keys():
        if key[0] == source_category:
            category_map = key
            target_category = key[1]
    
    if category_map == None:
        return value

    for map_entry in almanac[category_map]:
        source_range_start = map_entry[SOURCE_RANGE_START_POS]
        range_length = map_entry[RANGE_LENGTH_POS]
        if value in range(source_range_start,source_range_start+range_length):
            distance_from_start = value - source_range_start
            destination_range_start = map_entry[DESTINATION_RANGE_START_POS]
            return resolve(destination_range_start + distance_from_start, target_category, almanac)
    
    return resolve(value, target_category, almanac)

    # RESOLVE_SEED RECURSIVELY

def get_lowest_location(almanac):

    lowest_location = None
    
    for seed in almanac['seeds']:
        location = resolve(seed, 'seed', almanac) 
        if lowest_location == None or location < lowest_location:
            lowest_location = location

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
    # for key, value in almanac.items():
    #     print(key, value)

    print(get_lowest_location(almanac))
    print(datetime.now() - startTime)
