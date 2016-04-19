def fizz_buzz(n):
    i = 1
    items = []
    while i <= n:
        if i % 3 == 0 and i % 5 == 0:
            items.append("FizzBuzz")
        elif i % 3 == 0:
            items.append("Fizz")
        elif i % 5 == 0:
            items.append("Buzz")
        else:
            items.append(str(i))
        i += 1
    print(" ".join(items))


def fizz_buzz_alternate():
    items = []
    fizz = 3
    buzz = 5
    for i in range(1, 101):
        fizz -= 1
        buzz -= 1
        if fizz is 0 and buzz is 0:
            items.append("FizzBuzz")
            fizz = 3
            buzz = 5
        elif fizz is 0:
            items.append("Fizz")
            fizz = 3
        elif buzz is 0:
            items.append("Buzz")
            buzz = 5
        else:
            items.append(str(i))
    print (" ".join(items))

fizz_buzz(100)
fizz_buzz_alternate()
