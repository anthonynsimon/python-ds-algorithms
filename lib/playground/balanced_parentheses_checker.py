from lib.data_structures.stack import StackAI


class ParenthesesChecker:

    def __init__(self):
        self.__stack = StackAI()

    def check(self, data):
        balanced = True
        i = 0
        self.__stack.clear()
        while i < len(data) and balanced is not False:
            ch = data[i]
            if ch == "(":
                self.__stack.push(ch)
            elif ch == ")":
                if self.__stack.is_empty():
                    balanced = False
                else:
                    self.__stack.pop()
            i += 1

        if self.__stack.is_empty() is False:
            balanced = False
        return balanced
