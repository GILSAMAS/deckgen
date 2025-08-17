from prompteng.utils.files import get_config
from prompteng.utils.files import get_root_path

from pathlib import Path
def test_get_config():
    config = get_config("prompt_registry")
    assert config is not None

def test_get_root_path():
    """
    Test root path retrieval.
    """
    root_path = get_root_path()
    assert root_path is not None
    
