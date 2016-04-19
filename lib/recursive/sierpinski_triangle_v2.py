import turtle


def main(side_length, degrees):
    t = turtle.Turtle()
    window = turtle.Screen()
    t.hideturtle()
    t.speed("fastest")
    t.up()
    points = [[0, 0.865 * side_length / 2], [side_length / 2, -(0.865 * side_length / 2)], [-side_length / 2, -(0.865 * side_length / 2)]]
    draw_sierpinsky(t, degrees, points)
    window.exitonclick()


def draw_triangle(turtle, points):
    turtle.up()
    turtle.goto(points[0])
    turtle.down()
    turtle.goto(points[1])
    turtle.goto(points[2])
    turtle.goto(points[0])
    turtle.up()


def draw_sierpinsky(turtle, degree, points):
    draw_triangle(turtle, points)

    if degree > 0:
        degree -= 1

        p0 = [(points[0][0] + points[1][0]) / 2, (points[0][1] + points[1][1]) / 2]
        p1 = [(points[1][0] + points[2][0]) / 2, (points[1][1] + points[2][1]) / 2]
        p2 = [(points[2][0] + points[0][0]) / 2, (points[2][1] + points[0][1]) / 2]

        temp = [points[0], p0, p2]
        draw_sierpinsky(turtle, degree, temp)

        temp = [p0, points[1], p1]
        draw_sierpinsky(turtle, degree, temp)

        temp = [p1, points[2], p2]
        draw_sierpinsky(turtle, degree, temp)


main(400,6)