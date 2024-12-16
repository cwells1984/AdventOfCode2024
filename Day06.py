from enum import Enum
import numpy as np

GUARD_CHAR = ["^", "V", "<", ">"]
OBSTACLE_CHAR = ["#"]

class Facing(Enum):
    N = "^"
    S = "V"
    E = ">"
    W = "<"

class Room:

    def __init__(self, path):

        # Set up the grid
        grid = []
        with open(path, 'r') as f:
            for line in f.readlines():
                grid.append(list(line.strip()))
        grid = np.array(grid)
        self.shape = grid.shape

        # Work out the facing
        self.obstacles = set()
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):

                # Get the location of guards
                if grid[i][j] in GUARD_CHAR:
                    self.current_pos = (i, j)
                    self.visited_positions = set([self.current_pos])
                    if grid[i][j] == Facing.N.value:
                        self.current_facing = Facing.N
                    elif grid[i][j] == Facing.S.value:
                        self.current_facing = Facing.S
                    elif grid[i][j] == Facing.E.value:
                        self.current_facing = Facing.E
                    elif grid[i][j] == Facing.W.value:
                        self.current_facing = Facing.W

                # Get the location of obstacles
                if grid[i][j] in OBSTACLE_CHAR:
                    self.obstacles.add((i,j))

    def get_front_coords(self):
        front_coords = (-1,-1)

        if self.current_facing == Facing.N:
            front_coords = tuple(map(sum, zip(self.current_pos, (-1,0))))
        elif self.current_facing == Facing.S:
            front_coords = tuple(map(sum, zip(self.current_pos, (1,0))))
        elif self.current_facing == Facing.E:
            front_coords = tuple(map(sum, zip(self.current_pos, (0,1))))
        elif self.current_facing == Facing.W:
            front_coords = tuple(map(sum, zip(self.current_pos, (0,-1))))

        return front_coords

    def move(self):
        # If there is something in front of you, take a 90deg turn right
        front_coords = self.get_front_coords()

        # If we are going off the map, report it
        if front_coords[0] < 0 or front_coords[0] >= self.shape[0] or front_coords[1] < 0 or front_coords[1] >= self.shape[1]:
            return False

        # If there is something in front of you, take a 90deg turn right
        elif front_coords in self.obstacles:
            self.turn_right()
            return True

        # Otherwise, move forward
        else:
            self.current_pos = front_coords
            self.visited_positions.add(front_coords)
            return True

    def turn_right(self):
        if self.current_facing == Facing.N:
            self.current_facing = Facing.E
        elif self.current_facing == Facing.E:
            self.current_facing = Facing.S
        elif self.current_facing == Facing.S:
            self.current_facing = Facing.W
        elif self.current_facing == Facing.W:
            self.current_facing = Facing.N

    def print_room(self):
        for i in range(self.shape[0]):
            s = ""
            for j in range(self.shape[1]):
                if (i,j) in self.obstacles:
                    s += "#"
                elif self.current_pos == (i,j):
                    if self.current_facing == Facing.N:
                        s += Facing.N.value
                    elif self.current_facing == Facing.S:
                        s += Facing.S.value
                    elif self.current_facing == Facing.E:
                        s += Facing.E.value
                    elif self.current_facing == Facing.W:
                        s += Facing.W.value
                else:
                    s += "."
            print(s)
        print(f"{self.current_pos}, facing {self.current_facing}")
        print(f"Obstacles {self.obstacles}")


if __name__ == "__main__":

    # Part 1
    room = Room("Day06_input.txt")
    move_status = room.move()
    while move_status:
        # print("NEW MOVE")
        # room.print_room()
        # print(move_status)
        # print("==========")
        move_status = room.move()
    print(f"Part 1 - Visited {len(room.visited_positions)} positions")
