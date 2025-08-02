import os
from deckgen.reader.file_reader import FileReader
import tempfile


def create_temp_file(content: str, suffix: str = ".txt") -> str:
    """
    Create a temporary file with the given content and suffix.

    :param content: The content to write to the file.
    :param suffix: The file extension (default is .txt).
    :return: The path to the temporary file.
    """
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    temp_file.write(content.encode())
    temp_file.close()
    return temp_file.name


def test_read_text():
    """
    Test reading a text file using the FileReader class.
    """
    # Create a temporary text file for testing
    temp_file_path = create_temp_file("This is a test file.", suffix=".txt")
    try:
        # Initialize the FileReader with the temporary file path
        reader = FileReader(temp_file_path)

        # Read the content from the file
        content = reader.get_content()

        # Assert that the content is as expected
        assert content == "This is a test file."
    finally:
        # Clean up the temporary file
        os.remove(temp_file_path)


def test_file_extension_validation():
    """
    Test the file extension validation in the FileReader class.
    """
    # Create a temporary text file for testing
    temp_file_path_txt = create_temp_file("This is a test file.", suffix=".txt")
    # Create a temporary PDF file for testing
    temp_file_path_pdf = create_temp_file("This is a test PDF file.", suffix=".pdf")
    try:
        # Initialize the FileReader with the temporary file path
        reader_txt = FileReader(temp_file_path_txt)
        reader_pdf = FileReader(temp_file_path_pdf)

        # Validate the file extension
        assert reader_txt.file_extension == ".txt"
        assert reader_pdf.file_extension == ".pdf"
    finally:
        # Clean up the temporary file
        os.remove(temp_file_path_txt)
        os.remove(temp_file_path_pdf)


def test_invalid_file_extension():
    """
    Test that an error is raised when trying to read a file with an invalid extension.
    """
    # Create a temporary file with an unsupported extension
    temp_file_path = create_temp_file("This is a test file.", suffix=".docx")
    try:
        # Attempt to initialize the FileReader with the invalid file path
        reader = FileReader(temp_file_path)
        # If no exception is raised, the test should fail
        assert False, "Expected ValueError for unsupported file extension"
    except ValueError as e:
        # Assert that the correct error message is raised
        assert str(e) == "Invalid file type. Allowed types are: .txt, .pdf"
    finally:
        # Clean up the temporary file
        os.remove(temp_file_path)


def test_file_not_found():
    """
    Test that a FileNotFoundError is raised when trying to read a non-existent file.
    """
    # Use a non-existent file path
    non_existent_file_path = "non_existent_file.txt"
    try:
        # Attempt to initialize the FileReader with the non-existent file path
        reader = FileReader(non_existent_file_path)
        # If no exception is raised, the test should fail
        assert False, "Expected FileNotFoundError for non-existent file"
    except FileNotFoundError as e:
        # Assert that the correct error message is raised
        assert str(e) == f"The file {non_existent_file_path} does not exist."
