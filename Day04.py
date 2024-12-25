import numpy as np
import re

class TwoDArray():
    def __init__(self):
        self.grid = None
        self.shape = None

    @staticmethod
    def load_from_file(path):
        grid = []
        with open(path, 'r') as f:
            for line in f.readlines():
                grid.append(list(line.strip()))
        twod_array = TwoDArray()
        twod_array.grid = np.array(grid)
        twod_array.shape = twod_array.grid.shape
        return twod_array

    def get_row_strings(self):
        rows = []
        for i in range(self.shape[0]):
            rows.append("".join(self.grid[i,:]))
        return rows

    def get_col_strings(self):
        cols = []
        for i in range(self.shape[0]):
            cols.append("".join(self.grid[:, i]))
        return cols

    def get_diag_lr_strings(self):
        diags = []

        # Go from top left to top right
        for i in range(self.shape[1]):
            subgrid = self.grid[:,i:]
            diags.append("".join(list(subgrid.diagonal())))

        # Now go from top left + 1 to bottom left
        for i in range(1, self.shape[0]):
            subgrid = self.grid[i:,:]
            diags.append("".join(list(subgrid.diagonal())))

        return diags

    def get_diag_rl_strings(self):
        orig_grid = self.grid
        self.grid = np.fliplr(self.grid)
        flipped_diag_strings = self.get_diag_lr_strings()
        self.grid = orig_grid
        return flipped_diag_strings

    def get_a_subsets(self):
        a_locs = []
        a_subsets = []
        for i in range(1, grid.grid.shape[0] - 1):
            for j in range(1, grid.grid.shape[1] - 1):
                if grid.grid[i][j] == "A":
                    a_locs.append((i,j))
        for a_loc in a_locs:
            i = a_loc[0]
            j = a_loc[1]
            a_subsets.append(grid.grid[i-1:i+2, j-1:j+2])
        return a_subsets

    def count_xmas_crosses(self, subsets):
        num_crosses = 0
        for subset in subsets:
            diagonal_1 = []
            diagonal_1.append("".join(subset.diagonal()))
            diagonal_1.append("".join(np.fliplr(np.flipud(subset)).diagonal()))

            diagonal_2 = []
            diagonal_2.append("".join(np.flipud(subset).diagonal()))
            diagonal_2.append("".join(np.fliplr(subset).diagonal()))

            if "MAS" in diagonal_1 and "MAS" in diagonal_2:
                num_crosses += 1
        return num_crosses


def reverse_string(s):
    return s[::-1]

if __name__ == "__main__":

    # Part 1 code here
    grid = TwoDArray.load_from_file("Day04_Input.txt")
    rows = grid.get_row_strings()
    cols = grid.get_col_strings()
    diags_lr = grid.get_diag_lr_strings()
    diags_rl = grid.get_diag_rl_strings()

    total_found = 0
    for l in [rows, cols, diags_lr, diags_rl]:
        for s in l:
            found_xmas = re.findall("XMAS", s)
            total_found += len(found_xmas)
            s_rev = reverse_string(s)
            found_xmas = re.findall("XMAS", s_rev)
            total_found += len(found_xmas)

    print(f"Part 1 - Found {total_found} instances of 'XMAS'")

    # Part 2 code here
    grid = TwoDArray.load_from_file("Day04_Input.txt")
    subsets = grid.get_a_subsets()
    num_xmas = grid.count_xmas_crosses(subsets)
    print(f"Part 2 - Found {num_xmas} XMAS")
