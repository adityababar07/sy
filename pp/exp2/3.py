import math

# Loop to continuously prompt the user for shape selection
while True:
    print('''   
Select a shape from the below options:
      1) circle
      2) rectangle
      3) square
      4) triangle

Type 'exit' to exit.
''')

    choice = input("Enter your choice:\t")

    # Calculate area and circumference of a circle
    if choice == '1':
        radius = int(input("Enter the radius of the circle:\t"))
        print(f"Area of circle is {math.pi * radius ** 2}")
        print(f"Circumference of the circle is {2 * math.pi * radius}")

    # Calculate area and perimeter of a rectangle
    elif choice == '2':
        length = int(input("Enter the length of the rectangle:\t"))
        breadth = int(input("Enter the breadth of the rectangle:\t"))

        print(f"Area of rectangle is {length * breadth}")
        print(f"Perimeter of the rectangle is {2 * (length + breadth)}")

    # Calculate area and perimeter of a square
    elif choice == '3':
        length = int(input("Enter the length of the square:\t"))

        print(f"Area of square is {length ** 2}")
        print(f"Perimeter of the square is {4 * length}")

    # Calculate area and perimeter of a triangle
    elif choice == '4':
        height = int(input("Enter the height of the triangle:\t"))
        base = int(input("Enter the base of the triangle:\t"))
        side1 = int(input("Enter side 1:\t"))
        side2 = int(input("Enter side 2:\t"))

        print(f"Area of triangle is {1/2 * base * height}")
        print(f"Perimeter of the triangle is {base + side1 + side2}")

    # Exit the program if 'exit' is typed
    elif choice.lower() == "exit":
        exit()

    else:
        print("Your choice is invalid. Please choose the correct option.")
