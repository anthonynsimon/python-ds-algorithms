class Factorial(object):

    def __init__(self):
        self.__cache = {}
        self.__cache[0] = 1
        self.__cache[1] = 1

    def naiveFactorial(self, n):
        if n <= 1:
            return 1
        return (n * self.naiveFactorial(n-1))

    def topDown(self, n):
        if self.__cache.get(n):
            return self.__cache[n]

        for i in range(2,n+1):
            self.__cache[i] = i * self.__cache[i - 1]
        return self.__cache[n]


fact = Factorial()
for i in range(101):
    fact.topDown(i)
for element in fact.__cache:
    print("{0}! = {1}" .format(element, fact.__cache[element]))