from app.repositories.dataset_repository import DatasetRepository
from app.pipelines.prediction_pipeline import PredictionPipeline

repo = DatasetRepository()
print('messages rows', len(repo.messages))
print('users rows', len(repo.users))
print('history rows', len(repo.message_history))
print('events rows', len(repo.message_events))
print('sample message', repo.get_message('msg_023'))
print('building pipeline...')
pipeline = PredictionPipeline()
print('pipeline instantiated')
print('done')
