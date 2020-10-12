#!/usr/bin/python3#!/usr/bin/python3
"""
Square class that inherits from Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Representation of a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Calling the super class attributes"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Update the access with a new name"""
        return(self.width)

    @size.setter
    def size(self, value):
        """
        Width and height: assigned to the value of size
        """
        self.width = value
        self.height = value

    def area(self):
        """The area of the new object, square"""
        return(self.size * self.size)

    def __str__(self):
        """Format to print Square attributes"""
        return("[Square] ({:d}) {:d}/{:d} - {:d}".format
               (self.id, self.x, self.y, self.size))

    def update(self, *args, **kwargs):
        """Public method, that assigns attributes"""
        if len(args):
            for i, v in enumerate(args):
                if i == 0:
                    self.id = v
                elif i == 1:
                    self.size = v
                elif i == 2:
                    self.x = v
                elif i == 3:
                    self.y = v
        else:
            for value, key in enumerate(kwargs):
                if key == "id":
                    self.id = kwargs.get("id")
                elif key == "size":
                    self.size = kwargs.get("size")
                elif key == "x":
                    self.x = kwargs.get("x")
                elif key == "y":
                    self.y = kwargs.get("y")

    def to_dictionary(self):
        """Dictionary representation of square"""
        dict = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
        return(dict)
