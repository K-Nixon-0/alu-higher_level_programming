#!/usr/bin/python3
"""Defines a square"""
Rectangle = __import__('8-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square, inherits from Rectangle"""

    def __init__(self, size=0):
        super().__init__(size, size)
