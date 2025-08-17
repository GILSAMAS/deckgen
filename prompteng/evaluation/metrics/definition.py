from transformers import pipeline
from mlflow.metrics import MetricValue 
import pandas as pd 
from typing import List, Dict, Union

def toxicity_tr(text:Union[str, List[str]])->List[Dict[str, Union[str, float]]]:
    """
    Calculates the toxicity of the provided text
    tr is added to indicate that is calculated using transformers.

    :param text: The text to analyze.
    :return: The toxicity score of the text.
    """

    classifier = pipeline("text-classification", model="unitary/toxic-bert")

    if isinstance(text, str):
        text = [text]

    results = classifier(text)
    return results
    

