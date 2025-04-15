"""Simulate an instance of the river class."""

from .river import River

my_river: River = River(num_fish=10, num_bears=2)
"""Creating a new object in the River class."""
my_river.day = 0
my_river.view_river()
my_river.one_river_week()
