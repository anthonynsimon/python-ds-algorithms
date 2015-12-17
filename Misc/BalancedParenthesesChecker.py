from DataStructures import Stacks


class ParenthesesChecker:

    def __init__(self):
        self.__stack = Stacks.StackAI()

    def check(self, dataToCheck):
        balanced = True
        i = 0
        self.__stack.clear()
        while i < len(dataToCheck) and balanced is not False:
            ch = dataToCheck[i]
            if ch == "(":
                self.__stack.push(ch)
            elif ch == ")":
                if self.__stack.isEmpty():
                    balanced = False
                else:
                    self.__stack.pop()
            i += 1

        if self.__stack.isEmpty() is False:
            balanced = False
        return balanced