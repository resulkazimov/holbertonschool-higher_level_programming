#!/usr/bin/python3
"""
This module defines a Square class with private attribute size,
including getter and setter methods.
"""


class Square:
    """
    A class that defines a square by its size.
    """

    def __init__(self, size=0):
        """
        Initializes the square.

        Args:
            size (int): The size of the square's side.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the current square area.

        Returns:
            The current square area.
        """
        return self.__size ** 2
