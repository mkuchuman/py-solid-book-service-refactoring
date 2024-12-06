import json
import xml
import xml.etree.ElementTree
from abc import ABC, abstractmethod


class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, book: "Book") -> None:
        raise NotImplementedError


class ConsoleDisplay(DisplayStrategy):
    def display(self, book: "Book") -> None:
        print(book.content)


class ReverseDisplay(DisplayStrategy):
    def display(self, book: "Book") -> None:
        print(book.content[::-1])


class PrintStrategy(ABC):
    @abstractmethod
    def print(self, book: "Book") -> None:
        raise NotImplementedError


class ConsolePrint(PrintStrategy):
    def print(self, book: "Book") -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(PrintStrategy):
    def print(self, book: "Book") -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class SerializeStrategy(ABC):
    @abstractmethod
    def serialize(self, book: "Book") -> str:
        raise NotImplementedError


class JsonSerialize(SerializeStrategy):
    def serialize(self, book: "Book") -> json:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerialize(SerializeStrategy):
    def serialize(self, book: "Book") -> xml:
        root = xml.etree.ElementTree.Element("book")
        title = xml.etree.ElementTree.SubElement(root, "title")
        title.text = book.title
        content = xml.etree.ElementTree.SubElement(root, "content")
        content.text = book.content
        return xml.etree.ElementTree.tostring(root, encoding="unicode")


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title, self.content = title, content

    def display(self, display_type: str) -> None:
        if display_type == "reverse":
            strategy = ReverseDisplay()
        if display_type == "console":
            strategy = ConsoleDisplay()
        if strategy:
            strategy.display(self)
        else:
            raise ValueError(f"Unknown display type: {display_type}")

    def print_book(self, print_type: str) -> None:
        if print_type == "console":
            strategy = ConsolePrint()
        if print_type == "reverse":
            strategy = ReversePrint()
        if strategy:
            strategy.print(self)
        else:
            raise ValueError(f"Unknown print type: {print_type}")

    def serialize(self, serialize_type: str) -> None:
        if serialize_type == "json":
            strategy = JsonSerialize()
        if serialize_type == "xml":
            strategy = XmlSerialize()
        if strategy:
            return strategy.serialize(self)
        else:
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
