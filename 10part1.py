from datetime import datetime
import math
startTime = datetime.now()

def parse(input_data):
    lines = input_data.splitlines()

    return lines

def get_value(loc,grid):
    return grid[loc[0]][loc[1]]

def find_S(grid):
    for line_no, line in enumerate(grid):
        for col_no, char in enumerate(line):
            if char == "S":
                return (line_no, col_no)

VALUE_TO_DIRECTIONS = {
    "S" : "NSEW",
    "|" : "NS",
    "-" : "EW",
    "L" : "NE",
    "J" : "NW",
    "7" : "SW",
    "F" : "SE",
    "." : ""
}

DIRECTION_TO_REVERSE = {
    "S" : "N",
    "N" : "S",
    "E" : "W",
    "W" : "E"
}

def try_direction(direction, last_two, grid):
    last_pos = last_two[-1]
    previous_pos = last_two[0]

    if direction == "N":
        next_pos = (last_pos[0] - 1,last_pos[1])
    if direction == "S":
        next_pos = (last_pos[0] + 1,last_pos[1])
    if direction == "W":
        next_pos = (last_pos[0], last_pos[1] - 1)
    if direction == "E":
        next_pos = (last_pos[0], last_pos[1] + 1)
    
    if next_pos[0] == -1 or next_pos[1] == -1 or next_pos == previous_pos:
        return False
    else:
        reverse_direction = DIRECTION_TO_REVERSE[direction]
        next_pos_value = get_value(next_pos,grid)
        if reverse_direction in VALUE_TO_DIRECTIONS[next_pos_value]:
            return next_pos

    return False

def find_next(last_two, grid):
    last_pos = last_two[-1]

    directions = VALUE_TO_DIRECTIONS[get_value(last_pos,grid)]

    for direction in directions:
        result = try_direction(direction, last_two, grid)
        if result != False:
            return result

def generate_loop(grid):

    path_so_far = [ find_S(grid)]

    next_pos = find_next(path_so_far,grid)

    while next_pos != path_so_far[0]:
        path_so_far.append(next_pos)
        next_pos = find_next(path_so_far[-2:],grid)
    
    return path_so_far

if __name__ == "__main__":
    with open('10input.txt', 'r') as f:
        input_data = f.read()

#     input_data = """.....
# .S-7.
# .|.|.
# .L-J.
# .....
# """

#     input_data = """7-F7-
# .FJ|7
# SJLL7
# |F--J
# LJ.LJ"""

    grid = parse(input_data)
    loop = generate_loop(grid)
    # for pos in loop:
    #     print(pos)
    max_distance = int(len(loop)/2)
    print(max_distance)

    # S_loc = find_S(grid)
    # print(get_value(S_loc,grid))