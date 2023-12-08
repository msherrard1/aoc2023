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

#     input_data = """..616...............
# ...*....49.....-....
# ...863.....%.72.....
# .........171........
# ..............308..5
# ..............*.....
# .......582..335...26
# ......*.............
# ....827.............
# ........@......278*.
# .....990...........7
# ...................."""

    grid = load_matrix(input_data)
    part_numbers = find_part_numbers(grid)

    running_sum = 0
    for part_number in part_numbers:
        running_sum += part_number
    print(running_sum)