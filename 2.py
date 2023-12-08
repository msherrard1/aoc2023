def load_cube_set(cube_set_str):    
    cube_strings = cube_set_str.split(", ")
    cube_set = {}

    for cube_string in cube_strings:
        num_string, color_string = cube_string.split()
        cube_set[color_string] = int(num_string)

    return cube_set

def load_games(input_text):

    games = {}

    for line in input_text.splitlines():
        game_num_str, game_str = line.split(": ")

        game_num = int(game_num_str[5:])

        cube_set_strings = game_str.split("; ")

        cube_sets = []

        for cube_set_str in cube_set_strings:
            cube_sets.append(load_cube_set(cube_set_str))

        games[game_num] = cube_sets

    return games

def check_game(game, cube_bag):
    for cube_set in game:
        for color, num_cubes in cube_set.items():
            if num_cubes > cube_bag[color]:
                return False
    
    return True

with open('2input.txt', 'r') as f:
    input_data = f.read()

# input_data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# """

games = load_games(input_data)

# PART ONE

# cube_bag = {}

# cube_bag['red'] = 12
# cube_bag['green'] = 13
# cube_bag['blue'] = 14

# game_id_running_sum = 0

# for game_id, game in games.items():
#     if check_game(game, cube_bag):
#         game_id_running_sum += game_id

# print(game_id_running_sum)

# PART TWO

def find_game_minimum(game):
    min_cube_set = { 'red': 0, 'green': 0, 'blue': 0}

    for cube_set in game:
        for color, num_cubes in cube_set.items():
            if num_cubes > min_cube_set[color]:
                min_cube_set[color] = num_cubes
    
    return min_cube_set

running_sum = 0

for game in games.values():
    min_set = find_game_minimum(game)
    prod = 1
    for num_cubes in min_set.values():
        prod *= num_cubes
    running_sum += prod

print(running_sum)