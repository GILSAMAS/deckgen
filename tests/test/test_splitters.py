from deckgen.splitter.text_splitter import TextSplitter
from deckgen.splitter.document import Document


def test_text_splitter_by_length():
    """
    Test the TextSplitter class.
    """
    document = (
        "This is a test document. It has multiple lines.\nThis is the second line."
    )
    splitter = TextSplitter(document)

    # Test splitting by length
    documents = splitter.split_text(method="length", chunk_size=100)
    # verify that each document is classed as Document
    assert all(isinstance(doc, Document) for doc in documents)
    assert len(documents) == 1
    assert documents[0].get_content() == document


def test_text_splitter_by_delimiter():
    """
    Test the TextSplitter class with delimiter splitting.
    """
    # Test splitting by delimiter
    document = (
        "This is a test document. It has multiple lines.\nThis is the second line."
    )
    splitter = TextSplitter(document)
    delimiter_split = splitter.split_text(method="delimiter", delimiter="\n")
    # verify that each document is classed as Document
    assert all(isinstance(doc, Document) for doc in delimiter_split)
    assert len(delimiter_split) == 2
    assert (
        delimiter_split[0].get_content()
        == "This is a test document. It has multiple lines."
    )
    assert delimiter_split[1].get_content() == "This is the second line."
