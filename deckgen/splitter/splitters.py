from typing import List
from typing import Optional


class SimpleSplitter:
    """
    A simple splitter that splits text into chunks based on a specified size.
    """

    def split_by_length(self, text: str, chunk_size: int = 1000) -> List[str]:
        """
        Splits the input text into chunks of the specified length.

        :param text: The text to be split.
        :param chunk_size: The maximum length of each chunk. Default is 1000 characters.
        :return: A list of text chunks.
        """
        return [text[i : i + chunk_size] for i in range(0, len(text), chunk_size)]

    def split_by_delimiter(self, text: str, delimiter: str = "\n") -> List[str]:
        """
        Splits the input text into chunks based on the specified delimiter.

        :param text: The text to be split.
        :param delimiter: The delimiter to use for splitting. Default is newline character.
        :return: A list of text chunks.
        """
        return [line.strip() for line in text.split(delimiter) if line.strip()]

    def get_documents(self, text: str, method: str = "length", **kwargs) -> List[str]:
        """
        Splits the text based on the specified method.

        :param text: The text to be split.
        :param method: The method to use for splitting ('length' or 'delimiter').
        :return: A list of text chunks.
        :raises ValueError: If the method is not supported.
        """
        if method == "length":
            return self.split_by_length(text, chunk_size=kwargs.get("chunk_size", 1000))
        elif method == "delimiter":
            return self.split_by_delimiter(
                text, delimiter=kwargs.get("delimiter", "\n")
            )
        else:
            raise ValueError(f"Unsupported splitting method: {method}")
