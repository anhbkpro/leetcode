from datetime import datetime


class Greeter:
    def __init__(self, name: str) -> None:
        self.name = name

    def _day(self) -> str:
        return datetime.now().strftime("%A")

    def _part_of_day(self) -> str:
        current_hour = datetime.now().hour
        if current_hour < 12:
            return "morning"
        if 12 <= current_hour < 17:
            return "afternoon"
        return "evening"

    def greet(self, store: str) -> str:
        print(f"Hi, my name is {self.name}, and welcome to {store}!")
        print(f"How's your {self._day()} {self._part_of_day()} going?")
        print("Here's a coupon for 20% off!")


def main() -> None:
    greeter = Greeter("Andy")
    print(greeter.greet("Walmart"))


if __name__ == "__main__":
    main()
