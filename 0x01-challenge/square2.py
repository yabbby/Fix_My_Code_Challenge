#!/usr/bin/python3
"""creates more of a rectangle class"""


class Square():
    """Square or Rectangle Class"""

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """initialisation of class"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """perimeter of class"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """string representation of class"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """main function if called on terminal"""
    s = Square(height=12, width=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
