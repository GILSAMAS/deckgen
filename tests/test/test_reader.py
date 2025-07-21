import os
from deckgen.reader.file_reader import FileReader
import tempfile

def test_read_text():
    """
    Test reading a text file using the FileReader class.
    """
    # Create a temporary text file for testing
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp_file:
        temp_file.write(b"This is a test file.")
        temp_file_path = temp_file.name
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

