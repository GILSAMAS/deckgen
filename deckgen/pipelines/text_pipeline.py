from langchain_text_splitters import RecursiveCharacterTextSplitter
import pdfplumber
from typing import List
from pathlib import Path
from typing import Union
class TextPipeline:
    def __init__(self, file_path: Union[str, Path], chunk_size: int = 500, chunk_overlap: int = 0) -> None:
        self.file_path = Path(file_path) if isinstance(file_path, str) else file_path
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def _read_pdf(self) -> List[str]:
        """
        Reads a PDF file and extracts text from each page.

        :return: A list of strings, each representing the text from a page in the PDF.
        """
        if not self.file_path.exists() or not self.file_path.is_file():
            raise FileNotFoundError(
                f"The file {self.file_path} does not exist or is not a valid file."
            )

        with pdfplumber.open(self.file_path) as pdf:
            return [page.extract_text() for page in pdf.pages if page.extract_text()]

    def _generate_chunks(self, texts: List[str]) -> List[str]:
        """
        Uses langchain's RecursiveCharacterTextSplitter to split the text into smaller chunks.

        :param texts: A list of strings to be split into chunks.
        :return: A list of text chunks.
        """
        ch_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
            encoding_name="cl100k_base",
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
        )
        split_documents = []
        for document in texts:
            if not document or not document.strip():
                continue
            split_docs = ch_splitter.create_documents([document])
            split_documents.extend(split_docs)

        return split_documents

    def get_chunks(self) -> List[str]:
        """
        Retrieves text chunks from a PDF file by reading the file and splitting the text into manageable pieces.

        :return: A list of text chunks extracted from the PDF file.
        :raises ValueError: If no text is found in the PDF file or if no chunks
                    are generated from the text.
        :raises FileNotFoundError: If the specified PDF file does not exist or is not a valid file.
        """
        texts = self._read_pdf()
        if not texts:
            raise ValueError("No text found in the PDF file.")

        chunks = self._generate_chunks(texts)
        if not chunks:
            raise ValueError("No chunks generated from the text.")

        return chunks


# class TextSplitter:
#     def __init__(self, text: Optional[str] = None, *args, **kwargs) -> None:
#         """
#         Initializes the TextSplitter with the provided text and parameters for splitting.

#         :param text: The text to be split into smaller chunks.
#         :param args: Additional positional arguments (not used).
#         :param kwargs: Additional keyword arguments, including 'splitter_params' which can contain:
#                        - 'chunk_size': The size of each chunk (default is 100).
#                        - 'chunk_overlap': The overlap between chunks (default is 0).
#         """

#         self.text = text
#         self.splitter_params = kwargs.get("splitter_params", {})
#         self.chunk_size = self.splitter_params.get("chunk_size", 500)
#         self.chunk_overlap = self.splitter_params.get("chunk_overlap", 0)
#         self.ch_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
#             encoding_name="cl100k_base",
#             chunk_size=self.chunk_size,
#             chunk_overlap=self.chunk_overlap,
#         )

#     def get_documents(self, text: Optional[str] = None) -> List[str]:
#         """
#         Splits the input text into manageable chunks using the specified text splitter.
#         :return: A list of text chunks.
#         """
#         if not self.text:
#             if text is not None:
#                 self.text = text
#             else:
#                 raise ValueError("No input text provided for splitting.")

#         # Use the character text splitter to split each document into smaller chunks
#         split_documents = []
#         if isinstance(self.text, str):
#             self.text = [self.text]

#         for document in self.text:
#             if not document.strip():
#                 continue
#             split_docs = self.ch_splitter.create_documents([document])
#             split_documents.extend(split_docs)

#         return split_documents
