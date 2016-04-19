import turtle
import random


def branch_tree(length, t):
    if length > random.randrange(1,5):
        t.pensize(length/15)
        t.forward(length)
        rand_angle = random.randrange(15,45)
        t.left(rand_angle/2)
        branch_tree(length - random.randrange(15, 25), t)
        t.left(rand_angle/2)
        branch_tree(length - random.randrange(10, 20), t)
        t.right(rand_angle*1.5)
        branch_tree(length - random.randrange(10, 20), t)
        t.right(rand_angle/2)
        branch_tree(length - random.randrange(15, 25), t)
        t.left(rand_angle)
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
    branch_tree(random.randrange(70, 110), t)
    window.exitonclick()

main()
