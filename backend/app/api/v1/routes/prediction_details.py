from pathlib import Path

import pandas as pd
from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/prediction",
    tags=["Prediction Details"],
)


@router.get("/{message_id}")
def get_prediction(message_id: str):

    project_root = Path(__file__).resolve().parents[5]

    output_file = project_root / "output.csv"

    if not output_file.exists():
        raise HTTPException(
            status_code=404,
            detail="output.csv not found",
        )

    df = pd.read_csv(output_file)

    row = df[df["message_id"] == message_id]

    if row.empty:
        raise HTTPException(
            status_code=404,
            detail="Prediction not found",
        )

    return row.iloc[0].to_dict()