import json
import xml
import xml.etree.ElementTree
from abc import abstractmethod, ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.main import Book


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
