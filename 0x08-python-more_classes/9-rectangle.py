#!/usr/bin/python3
"""Define a Rectangle"""


class Rectangle:
    """Class Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area():
            return rect_1

        elif rect_1.area() > rect_2.area():
            return rect_1

        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance"""
        return cls(size, size)

    def __init__(self, width=0, height=0):
        """Instantiation object"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter property"""
        return self.__width

    @width.setter
    def width(self, value):
        """Define setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Define height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """Define setter height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Define area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Define Perimeter of rentangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """Prints the rectangle with a char"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join(str(self.print_symbol) * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """To be able to recreate a new instance"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """When an instance of the class is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
