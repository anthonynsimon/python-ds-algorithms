from DataStructures import Stacks


class HanoiDisk:
    def __init__(self, size):
        self.size = size

    def __int__(self):
        return self.size

    def __repr__(self):
        return str(self.size)

class Tower:
    def __init__(self):
        self.stack = Stacks.ALStack()

    def addToTop(self, disk):
        if self.stack.isEmpty() != True:
            if disk.size > int(self.stack.peek()):
                raise "Illegal move!"
                return
        self.stack.push(disk)

    def removeFromTop(self):
        if self.stack.isEmpty() != True:
            return self.stack.pop()
        else:
            print("Tower is empty.")

    def peekTop(self):
        return int(self.stack.peek())

    def __str__(self):
        return str(self.stack)

class TowersSet:
    def __init__(self, size):
        self.numberOfMoves = 0
        self.towerA = Tower()
        self.towerB = Tower()
        self.towerC = Tower()
        self.size = size
        for i in range(size):
            self.towerA.addToTop(HanoiDisk(size - i))
        self.solution = []
        for i in range(size):
            self.solution.append(size-i)

    def moveDisk(self, fromTower, toTower):
        if fromTower.stack.isEmpty():
            print("Tower is empty. Called on move {0}".format(self.numberOfMoves))
            return
        else:
            if toTower.stack.isEmpty():
                toTower.addToTop(fromTower.removeFromTop())
            else:
                if fromTower.peekTop() > toTower.peekTop():
                    raise "Illegal move!"
                    return
                else:
                    toTower.addToTop(fromTower.removeFromTop())
            self.numberOfMoves += 1

    def isSolved(self):
        if str(self.solution) == str(self.towerC.stack):
            return True
        else:
            return False

class HanoiSolver:
    def __init__(self, towers):
        self.towers = towers

    def solve(self):
        self.solveWorker(self.towers.towerA.stack.size(), self.towers.towerA, self.towers.towerC, self.towers.towerB)

    def solveWorker(self, height, source, destination, spare):
        if height >= 1:
            self.solveWorker(height-1, source, spare, destination)
            self.towers.moveDisk(source, destination)
            self.solveWorker(height-1, spare, destination, source)

towers = TowersSet(20)
hanoiSolver = HanoiSolver(towers)
hanoiSolver.solve()
print("Tower A = {0}" .format(towers.towerA))
print("Tower B = {0}" .format(towers.towerB))
print("Tower C = {0}" .format(towers.towerC))
print("{0}" .format("Problem solved!" if towers.isSolved() == True else "Problem not solved yet"))
if towers.isSolved():
    print("Required a minimum of {0} moves. Solved in {1} moves." .format(pow(2, towers.size) -1, towers.numberOfMoves))

