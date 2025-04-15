"""File to define Fish class."""


class Fish:
    """Define the fish class."""

    age: int

    def __init__(self):
        """Initialize the attributes for the fish class."""
        self.age = 0
        return None

    def one_day(self):
        """Define a function for one day in the river!"""
        self.age += 1
        return None
