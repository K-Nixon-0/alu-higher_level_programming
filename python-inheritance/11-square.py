#!/usr/bin/python3
"""Defines Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square inherits from Rectangle"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return [Square] size/size"""
        return "[Square] {}/{}".format(self._Rectangle__width,
                                        self._Rectangle__height)
