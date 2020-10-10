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
