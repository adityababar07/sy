import math

while True:
    print('''   

Select a shape from the below options:
      1) circle
      2) square
      3) rectangle
      4) triangle

!!!!!!!Type exit to exit.
''')

    choice = int(input("enter your choice:\t"))

    if choice == 1:
        radius = int(input("enter the radius of the circle:\t"))
        print(f"Area of circle is {math.pi * math.sqrt(radius)}")
        print(f"Circumferece of the circle is {2 * math.pi * radius}")

    elif choice == 2:
        length = int(input("enter the length of the rectangle:\t"))
        breadth = int(input("enter the breadth of the rectangle:\t"))

        print(f"Area of rectangle is {length * breadth}")
        print(f"perimeter of the rectangle is {2 * (length + breadth)}")

    elif choice == 3:
        length = int(input("enter the length of the square:\t"))

        print(f"Area of rectangle is {math.sqrt(length)}")
        print(f"perimeter of the rectangle is {4*length}")      

    elif choice == 4:
        height = int(input("enter the height of the triangle:\t"))
        base = int(input("enter the base of the triangle:\t"))
        side1 = int(input("enter side1:\t"))
        side2 = int(input("enter side2:\t"))


        print(f"Area of triangle is {1/2 * base * height}")
        print(f"perimeter of the triangle is {base+side1+side2}")

    elif choice == "exit":
        exit()

    else:
        print("your choice is invalid. Please choose the correct option.")