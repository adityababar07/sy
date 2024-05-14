# draw a polygon using turtle

import turtle

def polygon(pen, sides_of_polygon): 

    for _ in range(sides_of_polygon):
        pen.forward(100)
        pen.right(360/sides_of_polygon)
        

def main():

    pen = turtle.Turtle()

    screen = turtle.Screen()

    screen.setup(width=750, height=500)

    screen.title("polygon")

    sides_of_polygon = int(input("enter the sides of the polygon:\t"))

    polygon(pen, sides_of_polygon)

    turtle.done()

if __name__ == "__main__":
    main()