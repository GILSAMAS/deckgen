
import pandas as pd 
from prompteng.evaluation.metrics.definition import toxicity_tr
from mlflow.metrics import MetricValue 
import numpy as np

def custom_toxicity(predictions: pd.Series) -> MetricValue:
    """
    Compute the toxicity of the predictions against the predictions.

    :param predictions: The predicted labels.
    :return: A MetricValue object containing the toxicity scores.
    """    
    results = toxicity_tr(predictions.tolist())
    mean_tox = np.mean([r['score'] for r in results])  # Calculate mean toxicity score
    # Create MetricValue object
    metric_value = MetricValue(
        scores = [r['score'] for r in results],
        justifications = [r['label'] for r in results],
        aggregate_results = {
            "mean": mean_tox
        }
    )
    return metric_value