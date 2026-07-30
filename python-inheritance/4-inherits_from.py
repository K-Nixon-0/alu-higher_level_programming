#!/usr/bin/python3
"""Defines inherits_from function"""


def inherits_from(obj, a_class):
    """Return True if obj is instance of a class inherited from a_class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
