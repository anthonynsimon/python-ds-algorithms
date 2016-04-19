class Fibonacci(object):

    def __init__(self):
        self.__cache = {}
        self.__cache[0] = 1
        self.__cache[1] = 1

    def naive_fibonacci(self, n):
        if n == 0 or n == 1:
            return 1

        return self.naive_fibonacci(n - 1) + self.naive_fibonacci(n - 2)

    def bottom_up(self, n):
        for i in range(2, n + 1):
            self.__cache[i] = self.__cache[i - 1] + self.__cache[i - 2]
        return self.__cache[n]


fib = Fibonacci()
for i in range(200):
     # print(fib.naive_fibonacci(i))
     print(fib.bottom_up(i))