from pathlib import Path

import pandas as pd
from fastapi import APIRouter

router = APIRouter(
    prefix="/predictions",
    tags=["Predictions"],
)


@router.get("/")
def get_predictions():

    project_root = Path(__file__).resolve().parents[5]

    output_file = project_root / "output.csv"

    if not output_file.exists():
        return []

    df = pd.read_csv(output_file)

    return df.to_dict(orient="records")