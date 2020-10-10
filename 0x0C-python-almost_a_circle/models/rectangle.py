"""
Rectangle class that inherits from Base
"""


from models.base import Base


class Rectangle(Base):
    """Representation of a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Private instace attributes and using the super"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Access a private attribute"""
        return(self.__width)

    @width.setter
    def width(self):
        """Uptade private attribute"""
        self.__width = width

    @property
    def height(self):
        """Access a private attribute"""
        return(self.__height)

    @height.setter
    def height(self):
        """Uptade private attribute"""
        self.__height = height

    @property
    def x(self):
        """Access a private attribute"""
        return(self.__x)

    @x.setter
    def x(self):
        """Uptade private attribute"""
        self.__x = x

    @property
    def y(self):
        """Access a private attribute"""
        self.__y = y

    @height.setter
    def y(self):
        """Uptade private attribute"""
        self.__y = y
