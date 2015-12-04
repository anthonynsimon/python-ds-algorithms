from DataStructures import Stacks

class ParenthesesChecker:
    def __init__(self):
        self.stack = Stacks.ALIStack()

    def check(self, dataToCheck):
        balanced = True
        i = 0
        self.stack.clear()

        while i < len(dataToCheck) and balanced is not False:
            ch = dataToCheck[i]
            if ch == "(":
                self.stack.push(ch)
            elif ch == ")":
                if self.stack.isEmpty():
                    balanced = False
                else:
                    self.stack.pop()
            i += 1

        if self.stack.isEmpty() is False:
            balanced = False

        return balanced