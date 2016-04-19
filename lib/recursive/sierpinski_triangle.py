import turtle


def main():
    t = turtle.Turtle()
    window = turtle.Screen()
    t.speed("fastest")
    t.hideturtle()
    t.up()
    t.left(90)
    t.forward(200)
    t.left(30)
    t.down()
    draw(t, 450)
    window.exitonclick()


def draw(t, distance):
    if distance > 10:
        t.left(120)
        t.forward(distance)
        draw(t, distance // 2)
        t.left(120)
        t.forward(distance)
        draw(t, distance // 2)
        t.left(120)
        t.forward(distance)
        draw(t, distance // 2)


main()
