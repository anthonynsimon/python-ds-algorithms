from lib.data_structures import stack


class HanoiDisk(object):

    def __init__(self, size):
        self.size = size

    def __int__(self):
        return self.size

    def __repr__(self):
        return str(self.size)


class Tower(object):

    def __init__(self):
        self.stack = stack.StackAA()

    def add_to_top(self, disk):
        if not self.stack.is_empty():
            if disk.size > int(self.stack.peek()):
                raise "Illegal move!"
                return
        self.stack.push(disk)

    def remove_from_top(self):
        if not self.stack.is_empty():
            return self.stack.pop()
        else:
            print("Tower is empty.")

    def peek_top(self):
        return int(self.stack.peek())

    def __str__(self):
        return str(self.stack)


class TowersSet(object):

    def __init__(self, size):
        self.number_of_moves = 0
        self.tower_a = Tower()
        self.tower_b = Tower()
        self.tower_c = Tower()
        self.size = size
        for i in range(size):
            self.tower_a.add_to_top(HanoiDisk(size - i))

        self.solution = []
        for i in range(size):
            self.solution.append(size-i)

    def move_disk(self, from_tower, to_tower):
        if from_tower.stack.is_empty():
            print("Tower is empty. Called on move {0}".format(self.number_of_moves))
            return
        else:
            if to_tower.stack.is_empty():
                to_tower.add_to_top(from_tower.remove_from_top())
            else:
                if from_tower.peek_top() > to_tower.peek_top():
                    raise "Illegal move!"
                    return
                else:
                    to_tower.add_to_top(from_tower.remove_from_top())
            self.number_of_moves += 1

    def is_solved(self):
        if str(self.solution) == str(self.tower_c.stack):
            return True
        else:
            return False


class HanoiSolver(object):

    def __init__(self, towers):
        self.__towers = towers

    def solve(self):
        self.__solve_helper(self.__towers.tower_a.stack.size(), self.__towers.tower_a,
                            self.__towers.tower_c, self.__towers.tower_b)

    def __solve_helper(self, height, source, destination, spare):
        if height >= 1:
            self.__solve_helper(height - 1, source, spare, destination)
            self.__towers.move_disk(source, destination)
            self.__solve_helper(height - 1, spare, destination, source)


towers = TowersSet(16)
hanoiSolver = HanoiSolver(towers)
hanoiSolver.solve()
print("Tower A = {0}" .format(towers.tower_a))
print("Tower B = {0}" .format(towers.tower_b))
print("Tower C = {0}" .format(towers.tower_c))
print("{0}" .format("Problem solved!" if towers.is_solved() == True else "Problem not solved yet"))
if towers.is_solved():
    print("Required a minimum of {0} moves. Solved in {1} moves." .format(pow(2, towers.size) - 1,
                                                                          towers.number_of_moves))

