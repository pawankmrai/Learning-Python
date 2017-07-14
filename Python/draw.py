import turtle

def draw_square(some_turtle, angle):
    for i in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90 + angle)


def draw_art():
    # make window for square
    window = turtle.Screen()
    window.bgcolor("red")

    # get a drawing done here
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)

    # start square drawing
    angle = 0
    for i in range(1, 10):
        draw_square(brad, angle)
        angle = angle + 10

    # close window on click
    window.exitonclick()

draw_art()
