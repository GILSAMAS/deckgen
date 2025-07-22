from typing import List
from typing import Optional
from typing import Dict
from abc import ABC
from abc import abstractmethod


class BaseSplitter:
    """
    Base class for splitters.
    This class is intended to be extended by specific splitter implementations.
    It provides a structure for splitting documents into smaller parts.
    """

    def __init__(self, document):
        """
        Initializes the BaseSplitter with the provided document.

        :param document: The document to be split.
        """
        self.document = document

    @abstractmethod
    def split(self) -> List["Document"]:
        """
        Splits the document into smaller parts.
        This method should be implemented by subclasses.

        :return: A list of BaseDocument objects representing the split parts.
        """
        raise NotImplementedError("Subclasses must implement this method.")
