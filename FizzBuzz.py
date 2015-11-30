def FizzBuzz(maxN):
    n = 1
    while (n <= maxN):
        if (n % 3 == 0 and n % 5 == 0):
            print("FizzBuzz ")
        elif (n % 3 == 0):
            print("Fizz ")
        elif (n % 5 == 0):
            print("Buzz")
        else:
            print(n)
        n+=1

def FizzBuzzFaster():

    outString = ""
    fizz = 3
    buzz = 5

    for i in range(1,101):

        fizz -= 1
        buzz -= 1

        if fizz is 0 and buzz is 0:
            outString += "FizzBuzz "
            fizz = 3
            buzz = 5
        elif fizz is 0:
            outString += "Fizz "
            fizz = 3
        elif buzz is 0:
            outString += "Buzz "
            buzz = 5

        outString += str(i) + " "

    print(outString)

# FizzBuzz(100)
FizzBuzzFaster()