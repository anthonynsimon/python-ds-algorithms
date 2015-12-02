import turtle


def main(sideLength, degrees):
    t = turtle.Turtle()
    window = turtle.Screen()
    t.hideturtle()
    t.speed("fastest")
    t.up()
    points = [[0,0.865*sideLength/2],[sideLength/2,-(0.865*sideLength/2)],[-sideLength/2,-(0.865*sideLength/2)]]
    sierpinskiAlternative(t, degrees, points)
    window.exitonclick()


def drawTriangle(turtle,points):
    turtle.up()
    turtle.goto(points[0])
    turtle.down()
    turtle.goto(points[1])
    turtle.goto(points[2])
    turtle.goto(points[0])
    turtle.up()


def sierpinskiAlternative(turtle, degree, points):

    drawTriangle(turtle, points)

    if degree > 0:
        degree -= 1

        p0 = [(points[0][0] + points[1][0]) / 2, (points[0][1] + points[1][1]) / 2]
        p1 = [(points[1][0] + points[2][0]) / 2, (points[1][1] + points[2][1]) / 2]
        p2 = [(points[2][0] + points[0][0]) / 2, (points[2][1] + points[0][1]) / 2]

        temp = [points[0],p0,p2]
        sierpinskiAlternative(turtle, degree, temp)

        temp = [p0,points[1],p1]
        sierpinskiAlternative(turtle, degree, temp)

        temp = [p1,points[2],p2]
        sierpinskiAlternative(turtle, degree, temp)

main(400,6)