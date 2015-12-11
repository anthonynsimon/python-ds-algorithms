class Fibonacci(object):

    def __init__(self):
        self.cache = {}
        self.cache[0] = 1
        self.cache[1] = 1

    def naiveFibonacci(self, n):
        if n == 0 or n == 1:
            return 1

        return self.naiveFibonacci(n-1) + self.naiveFibonacci(n-2)

    def bottomUpFibonacci(self, n):
        for i in range(2, n + 1):
            self.cache[i] = self.cache[i-1] + self.cache[i-2]
        return self.cache[n]


fib = Fibonacci()
for i in range(200):
     #print(fib.naiveFibonacci(i))
     print(fib.bottomUpFibonacci(i))