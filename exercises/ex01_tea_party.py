"A program to help plan a cozy tea party!"


__author__: str = "730518756"


def main_planner(guests: int) -> None:
    "The entrypoint of the program!"
    print(f"A Cozy Tea Party for {guests} People!")
    print(f"Tea Bags: {tea_bags(people=guests)}")
    print(f"Treats: {treats(people=guests)}")
    print(f"Cost: ${cost(tea_bags(people=guests), treats(people=guests))}")


def tea_bags(people: int) -> int:
    "Calculate tea bags needed per person."
    return people * 2


def treats(people: int) -> int:
    "Calculate treats needed per person"
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    "Calculates tea and treat cost combined."
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
