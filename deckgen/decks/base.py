from typing import List
from typing import Dict
from typing import Optional
from typing import List
from typing import Union
from pathlib import Path
import pickle


class Deck:

    def __init__(self, name: str, description: Optional[str] = None):
        """
        Initializes a Deck with a name and an optional description.

        :param name: The name of the deck.
        :param description: An optional description of the deck.
        """
        self.name = name
        self.description = description if description is not None else ""
        self.cards: List[Card] = []

    def list_cards(self) -> List[Dict[str, str]]:
        """
        Lists all cards in the deck.

        :return: A list of dictionaries representing the cards in the deck.
                 Each dictionary contains 'front' and 'back' keys.
        """
        return [
            {"front": card.get_front(), "back": card.get_back()} for card in self.cards
        ]

    def add_card(self, card: "Card"):
        """
        Adds a card to the deck.

        :param card: The Card object to be added to the deck.
        """
        self.cards.append(card)

    def save(self, file_path: Union[str, Path]) -> None:
        """
        Saves the deck to a file.

        :param file_path: The path to the file where the deck will be saved.
        """
        with open(file_path, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def load(cls, file_path: Union[str, Path]) -> "Deck":
        """
        Loads a deck from a file.

        :param file_path: The path to the file from which the deck will be loaded.
        :return: A Deck object loaded from the file.
        """
        with open(file_path, "rb") as file:
            return pickle.load(file)


class Card:
    def __init__(self, front: str, back: str, tags: Optional[List[str]] = None):
        """
        Initializes a Card with a front and back.

        :param front: The front text of the card.
        :param back: The back text of the card.
        """
        self.front = front
        self.back = back
        self.tags = tags if tags is not None else []

    def get_front(self) -> str:
        """
        Returns the front text of the card.

        :return: The front text of the card.
        """
        return self.front

    def get_back(self) -> str:
        """
        Returns the back text of the card.

        :return: The back text of the card.
        """
        return self.back

    def get_tags(self) -> List[str]:
        """
        Returns the tags associated with the card.

        :return: List of tags associated with the card.
        """
        return self.tags
