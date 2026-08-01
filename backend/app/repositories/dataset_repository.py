from app.config.settings import settings
from app.services.ingestion.manager import DatasetManager


class DatasetRepository:

    def __init__(self):

        self.manager = DatasetManager(settings.DATASET_PATH)

    def get_messages(self):

        return self.manager.load("messages.csv")

    def get_users(self):

        return self.manager.load("users.csv")