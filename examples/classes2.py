class Square:
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    # This is a getter function. It will be invoked any time <mysquare>.height is called,
    # rather than directly accessing the value. Using a function enables us to perform
    # modifications on the return value, print output to the screen, etc. any time the value
    # is accessed.
    @property
    def height(self):
        print("Retrieving the height")
        return self.__height
    # This is a setter function. It will be invoked any time <mysquare>.height = ...
    # is called, rather than directly assigning the new value to self.height. This
    # is useful for validating new values.
    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("Please only enter numbers for height")

    @property
    def width(self):
        print("Retrieving the width")
        return self.__width

    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Please only enter numbers for width")

    def get_area(self):
        return int(self.__width) * int(self.__height)


def main():
    square = Square()
    height = input("Enter height: ")
    width = input("Enter width: ")
    square.height = height
    square.width = width
    print("Height:", square.height)
    print("Width:", square.width)
    print("The area is:", square.get_area())


main()