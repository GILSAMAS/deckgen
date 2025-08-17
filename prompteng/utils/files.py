from pathlib import Path
import yaml
from typing import Dict, Any

def get_root_path() -> Path:
    """
    Get the root path of the project.

    :return: Path object representing the root directory of the project.
    """
    return Path(__file__).parent.parent.parent

def get_config(name: str) -> Dict[str, Any]:
    """
    Get the configuration for a specific prompt.
    The yaml file should exist in the configs directory.

    :param name: The name of the prompt.
    :return: A dictionary containing the prompt configuration.
    """
    config_path = get_root_path() / "prompteng" / "configs" / f"{name}.yaml"

    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file {config_path} does not exist.")

    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config