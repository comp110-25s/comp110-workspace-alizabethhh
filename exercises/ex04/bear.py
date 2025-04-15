"""File to define Bear class."""


class Bear:
    """Define the bear class."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initialize the attributes for the bear class."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Define one day in the river function."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Bears have to eat! How many fish will they eat?"""
        self.hunger_score += num_fish
        return None
