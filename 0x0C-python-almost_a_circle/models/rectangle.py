#!/usr/bin/python3
"""
Rectangle class that inherits from Base
"""


from models.base import Base


class Rectangle(Base):
    """Representation of a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Private instace attributes and using the super"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Access a private attribute"""
        return(self.__width)

    @width.setter
    def width(self, width):
        """Uptade private attribute"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Access a private attribute"""
        return(self.__height)

    @height.setter
    def height(self, height):
        """Uptade private attribute"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Access a private attribute"""
        return(self.__x)

    @x.setter
    def x(self, x):
        """Uptade private attribute"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Access a private attribute"""
        return (self.__y)

    @y.setter
    def y(self, y):
        """Uptade private attribute"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Getting the area of the rectangle"""
        return(self.__width * self.__height)

    def display(self):
        """Prints in stdout the rectangle instance"""
        print("{}".format("\n" * self.__y), end="")
        for n in range(self.__height):
            print("{}{}".format(" " * self.__x, "#" * self.__width))

    def __str__(self):
        return ("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format
                (self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Assigns a key/value argument to attribute"""
        if len(args):
            """if args exists and it is not empty, skip kwargs"""
            for arg, value in enumerate((args)):
                if arg == 0:
                    self.id = value
                elif arg == 1:
                    self.__width = value
                elif arg == 2:
                    self.__height = value
                elif arg == 3:
                    self.__x = value
                elif arg == 4:
                    self.__y = value
        else:
            for value, key in enumerate(kwargs):
                if key == "id":
                    self.id = kwargs.get("id")
                if key == "width":
                    self.__width = kwargs.get("width")
                if key == "height":
                    self.__height = kwargs.get("height")
                if key == "x":
                    self.__x = kwargs.get("x")
                if key == "y":
                    self.__y = kwargs.get("y")

    def to_dictionary(self):
        """Returns a dictionary representation"""
        dict = {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
            }
        return(dict)
