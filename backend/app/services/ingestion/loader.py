from pathlib import Path

import pandas as pd


class DatasetLoader:
    def __init__(self, dataset_path: str):
        self.dataset_path = Path(dataset_path)

    def load_csv(self, filename: str):
        file_path = self.dataset_path / filename

        if not file_path.exists():
            raise FileNotFoundError(f"{filename} not found")

        return pd.read_csv(file_path)