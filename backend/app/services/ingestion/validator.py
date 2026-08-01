import pandas as pd


class DatasetValidator:

    @staticmethod
    def validate(df: pd.DataFrame):

        if df.empty:
            raise ValueError("Dataset is empty")

        if df.columns.duplicated().any():
            raise ValueError("Duplicate columns found")

        return True