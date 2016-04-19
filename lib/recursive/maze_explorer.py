# Todo:
# Change System to X,Y = 0,0 Bottom Left
# Add security check of having equal length rows

from copy import deepcopy

PART_OF_PATH = ' '
TRIED = 'x'
OBSTACLE = 'O'
PLAYER = 'P'
EXIT = 'E'

class Vector2D(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "[{0}, {1}]".format(self.x, self.y)


class Maze(object):

    def __init__(self, maze_file):
        self.grid = []
        self.player_position = Vector2D(0, 0)
        self.parse_maze(maze_file)

    def __repr__(self):
        items = []
        for row in self.grid:
            items.append("{0}".format(row))
        return "\n".join(items)

    def parse_maze(self, maze_file):
        maze_position = Vector2D(0,0)

        for line in open(maze_file):
            self.grid.append([])
            is_open = False
            for element in line:
                if element == '[':
                    is_open = True
                elif element == ']':
                    is_open = False
                elif is_open == True:
                    if element == PLAYER:
                        self.player_position = Vector2D(maze_position.x, maze_position.y)
                    self.grid[maze_position.y].append(element)
                    maze_position.x += 1
            maze_position.x = 0
            maze_position.y += 1

    def get_grid_cell(self, x, y):
        return self.grid[y][x]

    def set_grid_cell(self, x, y, value):
        self.grid[y][x] = value

    def movePlayer(self, new_position):
        new_cell = self.get_grid_cell(new_position.x, new_position.y)
        if new_cell == OBSTACLE:
            raise "OBSTACLE"
            return False
        elif new_cell == EXIT:
            return True

        self.set_grid_cell(self.player_position.x, self.player_position.y, PART_OF_PATH)
        self.set_grid_cell(new_position.x, new_position.y, PLAYER)
        self.player_position = Vector2D(new_position.x, new_position.y)
        return True


class MazeSolver:

    def __init__(self, maze):
        self.maze = maze
        self.paths_grid = deepcopy(self.maze.grid)

        if self.solve(self.maze.player_position):
            print("Maze solved!")
        else:
            print("Couldn't solve maze...")
        print(self)

    def __repr__(self):
        items = []
        for row in self.paths_grid:
            items.append("{0}".format(row))
        return "\n".join(items)

    def solve(self, vector):
        cell = self.paths_grid[vector.y][vector.x]
        if cell == EXIT:
            return True
        elif cell == TRIED or cell == OBSTACLE:
            return False

        self.paths_grid[vector.y][vector.x] = TRIED
        if self.solve(Vector2D(vector.x, vector.y-1)):
            return True
        elif self.solve(Vector2D(vector.x, vector.y+1)):
            return True
        elif self.solve(Vector2D(vector.x-1, vector.y)):
            return True
        elif self.solve(Vector2D(vector.x+1, vector.y)):
            return True


maze = Maze("./../../data/maze_map.txt")
solver = MazeSolver(maze)
