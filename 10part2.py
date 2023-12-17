from datetime import datetime
startTime = datetime.now()

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

class PipeMaze:

    def __init__(self,input_data):
        self.grid = self.parse(input_data)
        self.loop = self.generate_loop()

    def parse(self, input_data):
        lines = input_data.splitlines()
        return lines

    def get_value(self, loc):
        return self.grid[loc[0]][loc[1]]

    def find_S(self):
        for line_no, line in enumerate(self.grid):
            for col_no, char in enumerate(line):
                if char == "S":
                    return (line_no, col_no)

    def try_direction(self, direction, last_two):
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
            next_pos_value = self.get_value(next_pos)
            if reverse_direction in VALUE_TO_DIRECTIONS[next_pos_value]:
                return next_pos

        return False

    def find_next(self, last_two):
        last_pos = last_two[-1]

        directions = VALUE_TO_DIRECTIONS[self.get_value(last_pos)]

        for direction in directions:
            result = self.try_direction(direction, last_two)
            if result != False:
                return result

    def generate_loop(self):

        path_so_far = [ self.find_S()]

        next_pos = self.find_next(path_so_far)

        while next_pos != path_so_far[0]:
            path_so_far.append(next_pos)
            next_pos = self.find_next(path_so_far[-2:])
        
        return path_so_far

    def get_enclosed_area(self):
        #shoelace formula
        running_sum = 0

        next_points = self.loop[1:] + self.loop[0:1]

        for pt1, pt2 in zip(self.loop, next_points):
            running_sum += (pt1[0] * pt2[1]) - (pt1[1] * pt2[0])
        
        return running_sum / 2

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

#     input_data = """...........
# .S-------7.
# .|F-----7|.
# .||.....||.
# .||.....||.
# .|L-7.F-J|.
# .|..|.|..|.
# .L--J.L--J.
# ..........."""

#     input_data = """FF7FSF7F7F7F7F7F---7
# L|LJ||||||||||||F--J
# FL-7LJLJ||||||LJL-77
# F--JF--7||LJLJIF7FJ-
# L---JF-JLJIIIIFJLJJ7
# |F|F-JF---7IIIL7L|7|
# |FFJF7L7F-JF7IIL---7
# 7-L-JL7||F7|L7F-7F7|
# L.L7LFJ|||||FJL7||LJ
# L7JLJL-JLJLJL--JLJ.L"""

    pipe_maze = PipeMaze(input_data)

    area = pipe_maze.get_enclosed_area()
    print(area)

    # Pick's theorem
    points_inside = area - len(pipe_maze.loop)/2 + 1

    print(points_inside)

    print("--- %s seconds ---" % (datetime.now() - startTime))