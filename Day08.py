import numpy as np
import re

class Grid:
    def __init__(self, path):
        self.antennas_to_loc = {}
        self.loc_to_antenna = {}
        self.antinodes = set()

        with open(path, 'r') as f:

            # Set up the grid
            grid = []
            with open(path, 'r') as f:
                for line in f.readlines():
                    grid.append(list(line.strip()))
            grid = np.array(grid)
            self.shape = grid.shape

            # Get the locations of all the antennas
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    s = str(grid[i][j])
                    if re.match(r"([A-Z]|[a-z]|[0-9])", s):
                        self.loc_to_antenna[(i, j)] = s
                        if s in self.antennas_to_loc:
                            self.antennas_to_loc[s].append((i, j))
                        else:
                            self.antennas_to_loc[s] = [(i, j)]

            # Now calculate the antinodes
            antenna_pairs = []
            for k in self.antennas_to_loc.keys():
                antenna_locs = self.antennas_to_loc[k]
                for i in range(len(antenna_locs)):
                    for j in range(len(antenna_locs)):
                        if i != j:
                            antenna_pairs.append((antenna_locs[i], antenna_locs[j]))
            for antenna_pair in antenna_pairs:
                antinode = self.calculate_antinode(antenna_pair[0], antenna_pair[1])
                if antinode:
                    self.antinodes.add(antinode)

    def calculate_antinode(self, antenna1, antenna2):
        delta = tuple(x - y for x, y in zip(antenna1, antenna2))
        antinode = tuple(x - y for x, y in zip(antenna2, delta))

        if antinode[0] < 0 or antinode[0] >= self.shape[0] or antinode[1] < 0 or antinode[1] >= self.shape[1]:
            return None
        else:
            return antinode

    def print_grid(self):
        for i in range(self.shape[0]):
            s = ""
            for j in range(self.shape[1]):
                if (i,j) in self.loc_to_antenna:
                    s += self.loc_to_antenna[(i, j)]
                elif (i,j) in self.antinodes:
                    s += "#"
                else:
                    s += "."
            print(s)

if __name__ == "__main__":

    # Part 1
    grid = Grid("Day08_Input.txt")
    grid.print_grid()
    print(f"Part 1: {len(grid.antinodes)} unique anitnode locations")
