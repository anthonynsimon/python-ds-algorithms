# Todo:
# Change System to X,Y = 0,0 Bottom Left
# Add security check of having equal length rows

from copy import deepcopy

PART_OF_PATH = ' '
TRIED = 'x'
OBSTACLE = 'O'
PLAYER = 'P'
EXIT = 'E'

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "[{0},{1}]".format(self.x, self.y)

class Maze:
    def __init__(self,mazeFileName):
        self.grid = []
        self.playerPosition = Vector2D(0,0)
        self.parseMaze(mazeFileName)

    def __repr__(self):
        outString = ""
        for row in self.grid:
            outString += "{0}\n".format(row)
        return outString

    def parseMaze(self, mazeFile):
        mazePosition = Vector2D(0,0)
        for line in open(mazeFile):
            self.grid.append([])
            isOpen = False

            for element in line:
                if element == '[':
                    isOpen = True
                elif element == ']':
                    isOpen = False
                elif isOpen == True:
                    if element == PLAYER:
                        self.playerPosition = Vector2D(mazePosition.x, mazePosition.y)
                    self.grid[mazePosition.y].append(element)
                    mazePosition.x += 1
            mazePosition.x = 0
            mazePosition.y += 1

    def getGridCell(self,atX,atY):
        return self.grid[atY][atX]

    def setGridCell(self, atX, atY, value):
        self.grid[atY][atX] = value

    def movePlayer(self, newVector):
        newCell = self.getGridCell(newVector.x, newVector.y)
        if newCell == OBSTACLE:
            raise "OBSTACLE"
            return False
        elif newCell == EXIT:
            return True
        self.setGridCell(self.playerPosition.x,self.playerPosition.y, PART_OF_PATH)
        self.setGridCell(newVector.x, newVector.y, PLAYER)
        self.playerPosition = Vector2D(newVector.x, newVector.y)
        return True

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.pathsGrid = deepcopy(self.maze.grid)
        if self.solve(self.maze.playerPosition):
            print("Maze solved!")
        else:
            print("Couldn't solve maze...")
        print(self)

    def __repr__(self):
        outString = ""
        for row in self.pathsGrid:
            outString += "{0}\n".format(row)
        return outString

    def solve(self, vector):
        cell = self.pathsGrid[vector.y][vector.x]
        if cell == EXIT:
            return True
        if cell == TRIED or cell == OBSTACLE:
            return False
        self.pathsGrid[vector.y][vector.x] = TRIED

        if self.solve(Vector2D(vector.x, vector.y-1)):
            return True
        elif self.solve(Vector2D(vector.x, vector.y+1)):
            return True
        elif self.solve(Vector2D(vector.x-1, vector.y)):
            return True
        elif self.solve(Vector2D(vector.x+1, vector.y)):
            return True

maze = Maze("MazeMap.txt")
solver = MazeSolver(maze)