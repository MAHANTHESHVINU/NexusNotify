from dataclasses import asdict

from fastapi import APIRouter, HTTPException

from app.repositories.dataset_repository import DatasetRepository

router = APIRouter(
    prefix="/debug",
    tags=["Debug"]
)

repo = DatasetRepository()


@router.get("/message/{message_id}")
def get_message(message_id: str):

    message = repo.get_message(message_id)

    if message is None:
        raise HTTPException(status_code=404, detail="Message not found")

    return asdict(message)