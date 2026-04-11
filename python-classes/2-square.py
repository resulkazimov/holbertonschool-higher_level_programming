#!/usr/bin/python3
"""
This module defines a class Square with size validation.
"""


class Square:
    """
    A class that defines a square by its size with validation.
    """

    def __init__(self, size=0):
        """
        Initializes the square with a validated size.

        Args:
            size (int): The size of the square's side.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
