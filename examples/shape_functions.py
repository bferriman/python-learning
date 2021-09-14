import math


def get_area(shape):
    shape = shape.lower()
    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print("Please enter 'rectangle' or 'circle'")


def rectangle_area():
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = length * width
    print("Area of rectangle =", area)


def circle_area():
    radius = float(input("Enter radius: "))
    area = math.pi * (math.pow(radius, 2))
    print("Area of circle = {:.2f}".format(area))


def main():  # it is common to define main program login in 'main' function, to be invoked on program start
    shape_type = input("Get area for what shape?: ")
    get_area(shape_type)


main()
