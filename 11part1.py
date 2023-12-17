import itertools
from datetime import datetime
startTime = datetime.now()

class TelescopeImage:

    def __init__(self, input_data) -> None:
        input_data_expanded = self.expand(input_data)
        self.galaxies = self.parse_galaxies(input_data_expanded)

    def galaxy_distances(self):
        galaxy_pairs = itertools.combinations(self.galaxies,2)
        
        galaxy_pair_distances = {}

        for galaxy_pair in galaxy_pairs:
            galaxy_pair_distances[galaxy_pair] = self.get_distance(galaxy_pair[0], galaxy_pair[1])

        return galaxy_pair_distances

    @staticmethod
    def get_distance(galaxy1, galaxy2):
        return abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])

    @staticmethod
    def parse_galaxies(input_data):
        lines = input_data.splitlines()
        galaxies = []

        for row_id, line in enumerate(lines):
            for col_id, char in enumerate(line):
                if char == '#':
                    galaxy = (row_id, col_id)
                    galaxies.append(galaxy)

        return galaxies

    @staticmethod
    def expand(input_data):
        lines = input_data.splitlines()
        lines_rows_expanded = []
        galaxy_col_ids = []

        for line in lines:
            galaxy_col_ids_in_line = []

            for col_id, char in enumerate(line):
                if char == "#":
                    galaxy_col_ids_in_line.append(col_id)

            lines_rows_expanded.append(line)
            if galaxy_col_ids_in_line == []:
                lines_rows_expanded.append(line)

            galaxy_col_ids += galaxy_col_ids_in_line

        galaxy_col_ids = set(galaxy_col_ids)
        
        lines_cols_expanded = []
        
        for line in lines_rows_expanded:
            expanded_line = ""
            for col_id, char in enumerate(line):
                expanded_line += char
                if col_id not in galaxy_col_ids:
                    expanded_line += char
            lines_cols_expanded.append(expanded_line)

        return '\n'.join(lines_cols_expanded)

if __name__ == "__main__":
    with open('11input.txt', 'r') as f:
        input_data = f.read()

#     input_data = """...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#.....
#     """

    telescope_image = TelescopeImage(input_data)
    pair_distances = telescope_image.galaxy_distances()

    running_sum = 0
    for pair, distance in pair_distances.items():
        running_sum += distance
    print(running_sum)
    print("--- %s seconds ---" % (datetime.now() - startTime))