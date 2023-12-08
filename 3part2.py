import re

def load_matrix(input_data):
    grid = []
    for line in input_data.splitlines():
        grid.append(line)
    
    return grid

def is_symbol(char):
    if char in ".0123456789":
        return False
    else:
        return True

def check_for_part(line_number, span, grid):
    
    # where to search for symbols
    lines = [line_number - 1, line_number, line_number + 1]
    cols = range(span[0] - 1, span[1] + 1)

    for line in lines:
        # is line in bounds?
        if line >= 0 and line < len(grid):
            for col in cols:
                if col >= 0 and col < len(grid[line]):
                    char = grid[line][col]
                    if is_symbol(char) == True:
                        return True

    return False

def find_part_numbers(grid):
    part_numbers = []

    for line_number, line in enumerate(grid):
        for number_match in re.finditer(r"\d+", line):
            span = number_match.span()
            number = int(number_match.group(0))
            if check_for_part(line_number, span, grid) == True:
                part_numbers.append(number)

    return part_numbers

def check_asterisk(asterisk, grid):
    line_number = asterisk[0]
    col_number = asterisk[1]

    if line_number == 0:
        lines = grid[0:2]
    else:
        lines = grid[line_number-1:line_number+2]

    nums_found = []
    for line in lines:
        for number_match in re.finditer(r"\d+", line):
            start_pos, end_pos = number_match.span()
            number = int(number_match.group(0))
            if col_number in range(start_pos-1,end_pos+1):
                nums_found.append(number)
    
    if len(nums_found) == 2:
        return nums_found
    else:
        return False

def find_gears(grid):
    asterisks_found = []

    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == "*":
                asterisks_found.append((y,x))

    gears_found = {}

    for asterisk in asterisks_found:
        result = check_asterisk(asterisk,grid)
        if result != False:
            gears_found[asterisk] = result

    return gears_found

if __name__ == "__main__":
    with open('3input.txt', 'r') as f:
        input_data = f.read()
    
#     input_data = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
#     """

    grid = load_matrix(input_data)
    gears = find_gears(grid)
    
    running_sum = 0
    for loc, pair in gears.items():
        running_sum += pair[0]*pair[1]
    print(running_sum)