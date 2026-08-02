from app.pipelines.prediction_pipeline import PredictionPipeline
from app.services.export.csv_exporter import CSVExporter


pipeline = PredictionPipeline()

predictions = pipeline.run()

CSVExporter().export(
    predictions,
    "../output.csv",
)

print("Prediction pipeline completed.")