import mlflow  
from prompteng.utils.files import get_config

def get_prompt(name:str, alias: str, version: str)-> str:
    """
    Interface for retrieving prompts from the MLflow Prompt Registry.

    Either 'alias' or 'version' must be provided, but not both. If both are provided,
    the function will prioritize using the alias.

    :param name: Name of the prompt.
    :param alias: Alias for the prompt.
    :param version: Version of the prompt.
    :return: The retrieved prompt as a string.
    :raises ValueError: If the alias is not valid.
    :raises ValueError: If both 'alias' and 'version' are not provided.
    :raises MLflowException: If there is an error retrieving the prompt.
    """

    if not _validate_alias(alias):
        raise ValueError(f"Alias '{alias}' is not one of the allowed aliases.")

    if alias:
        prompt_uri = f"prompts:/{name}/{alias}"
    elif version:
        prompt_uri = f"prompts:/{name}/{version}"
    else:
        raise ValueError("Either 'alias' or 'version' must be provided.")

    prompt = mlflow.genai.load_prompt(prompt_uri)

    return prompt

def _validate_alias(alias: str) -> bool:
    """
    This function checks if the provided alias is valid.

    :param alias: The alias to validate.
    :return: True if the alias is valid, False otherwise.
    """
    # Implement your alias validation logic here
    allowed_aliases = get_config("prompt_registry").get("aliases", [])
    print(f"Validating alias: {alias}, Allowed aliases: {allowed_aliases}")
    return alias in allowed_aliases