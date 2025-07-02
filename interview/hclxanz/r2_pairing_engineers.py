from collections import defaultdict


def engineerPairs(engineers, cycleTeams):
    # Initialize available engineers for each engineer
    available_engineers = {eng: set(engineers) - {eng} for eng in engineers}

    # Process each team to remove paired engineers
    for team in cycleTeams:
        team_set = set(team)
        for engineer in team_set:
            # Remove all engineers from the current team from available engineers
            available_engineers[engineer] -= team_set

    # Convert sets to sorted lists for final output
    return {
        eng: sorted(list(available)) for eng, available in available_engineers.items()
    }


def main():
    engineers = [
        "Alice",
        "Bob",
        "Charlie",
        "Deepak",
        "Eve",
        "Fred",
        "Gao",
        "Han",
        "Ishika",
        "John",
    ]

    cycleTeams = [
        ["Eve", "Fred", "Ishika", "Deepak", "Han"],
        ["Charlie", "Alice"],
        ["Fred", "Gao"],
        ["John", "Deepak", "Ishika", "Alice"],
        ["Eve", "Charlie", "Han", "Bob", "Fred"],
        ["Deepak", "Gao", "Han"],
        ["Bob", "Fred", "John", "Ishika"],
        ["John", "Charlie", "Eve"],
        ["Bob", "Gao", "Alice", "Han"],
        ["Fred", "Charlie", "Bob"],
    ]

    result = engineerPairs(engineers, cycleTeams)

    # Print results in a readable format
    for engineer, available in result.items():
        print(f"{engineer}: {available}")


if __name__ == "__main__":
    main()
