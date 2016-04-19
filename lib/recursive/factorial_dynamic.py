class Factorial(object):

    def __init__(self):
        self.cache = {}
        self.cache[0] = 1
        self.cache[1] = 1

    def naive_factorial(self, n):
        if n <= 1:
            return 1
        return n * self.naive_factorial(n - 1)

    def top_down(self, n):
        if self.cache.get(n):
            return self.cache[n]

        for i in range(2,n+1):
            self.cache[i] = i * self.cache[i - 1]
        return self.cache[n]


fact = Factorial()
for i in range(1000):
    fact.top_down(i)
for element in fact.cache:
    print("{0}! = {1}" .format(element, fact.cache[element]))