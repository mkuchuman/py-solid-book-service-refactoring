from app.displays import ReverseDisplay, ConsoleDisplay
from app.prints import ConsolePrint, ReversePrint
from app.serializers import JsonSerialize, XmlSerialize


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title, self.content = title, content

    def display(self, display_type: str) -> None:
        if display_type == "reverse":
            strategy = ReverseDisplay()
        if display_type == "console":
            strategy = ConsoleDisplay()
        if strategy:
            return strategy.display(self)
        raise ValueError(f"Unknown display type: {display_type}")

    def print_book(self, print_type: str) -> None:
        if print_type == "console":
            strategy = ConsolePrint()
        if print_type == "reverse":
            strategy = ReversePrint()
        if strategy:
            return strategy.print(self)
        raise ValueError(f"Unknown print type: {print_type}")

    def serialize(self, serialize_type: str) -> None:
        if serialize_type == "json":
            strategy = JsonSerialize()
        if serialize_type == "xml":
            strategy = XmlSerialize()
        if strategy:
            return strategy.serialize(self)
        raise ValueError(f"Unknown serialize type: {serialize_type}")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            book.display(method_type)
        elif cmd == "print":
            book.print_book(method_type)
        elif cmd == "serialize":
            return book.serialize(method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
