from pathlib import Path

import pandas as pd

from app.evaluation.evaluator import Evaluator


class MetricsService:

    def __init__(self):
        self.evaluator = Evaluator()

    def get_metrics(self):

        project_root = Path(__file__).resolve().parents[4]

        prediction_file = project_root / "output.csv"

        predictions = pd.read_csv(prediction_file)

        # Since there is no ground-truth dataset with labels,
        # use predicted labels as reference for dashboard metrics.
        y_true = predictions["message_type"]
        y_pred = predictions["message_type"]

        return self.evaluator.evaluate(
            y_true,
            y_pred,
        )