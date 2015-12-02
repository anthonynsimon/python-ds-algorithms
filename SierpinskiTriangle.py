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
    drawSierpinskiTriangle(t,450)
    window.exitonclick()

def drawSierpinskiTriangle(t, distance):
    if distance > 10:
        t.left(120)
        t.forward(distance)
        drawSierpinskiTriangle(t,distance//2)
        t.left(120)
        t.forward(distance)
        drawSierpinskiTriangle(t,distance//2)
        t.left(120)
        t.forward(distance)
        drawSierpinskiTriangle(t,distance//2)

main()