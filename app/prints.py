from abc import ABC, abstractmethod


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
