# BEFORE COMMIT RUN THE SCRIPT TO GENERATE THE .YAML FILES WITH THE PROMPTS THAT ARE
# USED IN THE DECKGEN PACKAGE.
from ml_extra.decorators.mlflow.exp_tracking import mlflow_experiment
from ml_extra.decorators.mlflow.exp_tracking import mlflow_client
from ml_extra.decorators.mlflow.exp_tracking import mlflow_tracking_uri
import mlflow
import yaml
import os

def get_prompt_by_alias(prompt_name: str, alias: str) -> mlflow.genai.PromptVersion:
    """
    Retrieves a prompt by its alias from MLflow.

    :param prompt_name: The name of the prompt to retrieve.
    :param alias: The alias of the prompt version to retrieve.
    :return: The prompt version object.
    :raises ValueError: If the prompt with the specified name and alias does not exist.
    """
    prompt_uri = f"prompts:/{prompt_name}@{alias}"
    prompt_version = mlflow.genai.load_prompt(name_or_uri=prompt_uri)
    if not prompt_version:
        raise ValueError(
            f"Prompt '{prompt_name}' with alias '{alias}' not found in MLflow."
        )
    return prompt_version

def write_prompt_to_deckgen(prompt: mlflow.genai.PromptVersion) -> None:
    """
    Writes the prompt template to a YAML file in the deckgen/templates directory.

    :param prompt: The prompt version object containing the template.
    :return: None
    """
    file_path = f"deckgen/templates/templates.yaml"
    # Ensure the directory exists   
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # open the yaml file as dictionary
    with open(file_path, "rb") as f:
        prompt_templates = yaml.safe_load(f) or {}

    # Update the dictionary with the prompt template.
    # if the prompt already exists, it will be updated.
    prompt_templates.update({prompt.name: prompt.template})

    # Write the updated dictionary back to the YAML file
    with open(file_path, "w") as f:
        yaml.dump(prompt_templates, f)

if __name__ == "__main__":
    prompt_name = "question_asker_prompt"
    prompt = get_prompt_by_alias(
        prompt_name=prompt_name, alias="v1"
    )
    write_prompt_to_deckgen(prompt=prompt)