#!/usr/bin/python3
"""Module that prints a text with 2 new lines after ., ? and :"""


def text_indentation(text):
    """Print text with 2 new lines after each ., ? or :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    marks = ".?:"
    line = ""
    for char in text:
        if char == " " and line == "":
            continue
        line += char
        if char in marks:
            print(line.strip())
            print()
            line = ""
    if line.strip():
        print(line.strip(), end="")
