#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Get/set the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return current area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Print square with # based on size"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("#" * self.__size)
