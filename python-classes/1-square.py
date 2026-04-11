#!/usr/bin/python3
"""
This module defines a class Square with a private instance attribute size.
"""


class Square:
    """
    A class that defines a square by its size.
    """

    def __init__(self, size):
        """
        Initializes the square with a private size attribute.

        Args:
            size: The size of the square's side.
        """
        self.__size = size
