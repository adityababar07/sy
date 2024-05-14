# draw a parallelogram using turtle

import turtle

screen = turtle.Screen()

screen.setup(width=750, height=400)

screen.title("rectangle")

pen = turtle.Turtle()

for i in range(2):
    pen.forward(200)
    pen.right(60)
    pen.forward(100)
    pen.right(120)

turtle.done()
