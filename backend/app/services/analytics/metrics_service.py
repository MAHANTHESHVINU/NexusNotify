from pathlib import Path

import pandas as pd

from app.evaluation.evaluator import Evaluator


class MetricsService:

    def __init__(self):
        self.evaluator = Evaluator()

    def get_metrics(self):

        # Project root = NexusNotify/
        project_root = Path(__file__).resolve().parents[4]

        prediction_file = project_root / "output.csv"
        truth_file = project_root / "datasets" / "messages.csv"

        print("Prediction:", prediction_file)
        print("Dataset:", truth_file)

        print(prediction_file.exists())
        print(truth_file.exists())

        predictions = pd.read_csv(prediction_file)
        truth = pd.read_csv(truth_file)

        print(predictions.columns.tolist())
        print(truth.columns.tolist())

        merged = predictions.merge(
            truth,
            on="message_id",
            suffixes=("_pred", "_true"),
        )

        y_true = merged["message_type_true"]
        y_pred = merged["message_type_pred"]

        return self.evaluator.evaluate(
            y_true,
            y_pred,
        )