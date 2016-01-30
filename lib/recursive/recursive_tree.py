import turtle
import random

def branchTree(length, t):
    if length > random.randrange(1,5):
        t.pensize(length/15)
        t.forward(length)
        randAngle = random.randrange(15,45)
        t.left(randAngle/2)
        branchTree(length-random.randrange(15,25), t)
        t.left(randAngle/2)
        branchTree(length-random.randrange(10,20), t)
        t.right(randAngle*1.5)
        branchTree(length-random.randrange(10,20),t)
        t.right(randAngle/2)
        branchTree(length-random.randrange(15,25),t)
        t.left(randAngle)
        t.up()
        t.back(length)
        t.down()

def main():
    t = turtle.Turtle()
    window = turtle.Screen()
    t.hideturtle()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.speed(100000)
    turtle.tracer(0,0)
    branchTree(random.randrange(70,110),t)
    window.exitonclick()

main()
