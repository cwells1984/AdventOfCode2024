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


