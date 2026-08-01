from app.services.ingestion.loader import DatasetLoader
from app.services.ingestion.validator import DatasetValidator


class DatasetManager:

    def __init__(self, dataset_path):

        self.loader = DatasetLoader(dataset_path)

    def load(self, filename):

        df = self.loader.load_csv(filename)

        DatasetValidator.validate(df)

        return df