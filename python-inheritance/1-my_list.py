#!/usr/bin/python3
"""Defines a MyList class"""


class MyList(list):
    """MyList inherits from list"""

    def print_sorted(self):
        """Print the list, sorted (ascending)"""
        print(sorted(self))
