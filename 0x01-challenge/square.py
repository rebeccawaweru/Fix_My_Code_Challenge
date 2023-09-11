#!/usr/bin/python3
"""Square module"""


class Square():
    """Square module documentation"""
    def __init__(self, width=0, height=0):
        """Initialization"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width"""
        return self.__width

    @property
    def height(self):
        """height"""
        return self.height

    @width.setter
    def width(self, value):
        """width setter"""
        if value < 1:
            raise ValueError('Width must be greater than 0')
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """height setter"""
        if value < 1:
            raise ValueError('Height must be greater than 0')
        else:
            self.__height = value

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """Perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """String representation of the Square"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
