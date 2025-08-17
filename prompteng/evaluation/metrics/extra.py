import mlflow 
from prompteng.evaluation.metrics.custom import custom_toxicity

class ExtraMetrics:

    __available_metrics = {
        "custom_toxicity": {
            "name":"custom_toxicity",
            "eval_fn": custom_toxicity,
            "greater_is_better": False
        }
    }

    @classmethod
    def get_metric(cls, name: str):
        """
        Returns the metric by name.
        
        :param name: The name of the metric to retrieve.
        :return: The metric function or None if not found.
        """

        metric_config = cls.__available_metrics.get(name)
        if not metric_config:
            return None

        custom_metric = mlflow.metrics.make_metric(
            name=metric_config["name"],
            eval_fn=metric_config["eval_fn"],
            greater_is_better=metric_config["greater_is_better"]
        )

        return custom_metric