#!/usr/bin/python3
"""Defines write_file function"""


def write_file(filename="", text=""):
    """Write a string to a text file and return the number of chars written"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
