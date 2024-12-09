from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.main import Book


class PrintStrategy(ABC):
    @abstractmethod
    def print(self, book: "Book") -> None:
        raise NotImplementedError


class ConsolePrint(PrintStrategy):
    def print(self, book: "Book") -> None:
        print(f"Printing the book: {book.title}...\n{book.content}")


class ReversePrint(PrintStrategy):
    def print(self, book: "Book") -> None:
        print(f"Printing the book in reverse: {book.title}..."
              f"\n{book.content[::-1]}")
