"""File to define River class."""

__author__: str = "730518756"


from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:
    """Define the river class."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(
        self, num_fish: int, num_bears: int
    ):  # Initialize attributes for the river class.
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Update the lists of animals by removing ones that are too old."""
        livingbears: list[Bear] = []
        idx_bear: int = 0
        while idx_bear < len(self.bears):

            if self.bears[idx_bear].age <= 5:
                livingbears.append(self.bears[idx_bear])

            idx_bear += 1

        self.bears = livingbears
        idx_fish = 0
        livingfish: list[Fish] = []

        while idx_fish < len(self.fish):

            if self.fish[idx_fish].age <= 3:
                livingfish.append(self.fish[idx_fish])

            idx_fish += 1

        self.fish = livingfish

        return None

    def bears_eating(self):
        """How much are the bears eating?"""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)  # Remove 3 fish from the river
                bear.eat(3)  # Bear eats 3 fish

        return None

    def check_hunger(self):
        """How hungry are the bears?"""
        bearsthatdidnotstarve: list[Bear] = []
        idx: int = 0
        while idx < len(self.bears):

            if self.bears[idx].hunger_score < 0:
                bearsthatdidnotstarve.append(self.bears[idx])

            idx += 1

        self.bears = bearsthatdidnotstarve
        return None

    def repopulate_fish(self):
        """Adding more fish to the river."""
        new_fish: int = (len(self.fish) // 2) * 4
        for _ in range(0, new_fish):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Adding more bears to the river."""
        new_bears: int = len(self.bears) // 2
        for _ in range(0, new_bears):
            self.bears.append(Bear())
        return None

    def view_river(self):
        """Let's take a look at the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Let's take a look at one week in the river."""
        idx: int = 0
        while idx < 7:
            self.one_river_day()
            idx += 1

        return None

    def remove_fish(self, amount: int):
        """Some fish are removed."""
        idx = 0
        while idx < amount and len(self.fish) > 0:
            self.fish.pop(0)
            idx += 1

            return None
