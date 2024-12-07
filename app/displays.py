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
