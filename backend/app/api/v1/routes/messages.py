from fastapi import APIRouter

from app.repositories.dataset_repository import DatasetRepository

router = APIRouter(
    prefix="/messages",
    tags=["Messages"],
)

repo = DatasetRepository()


@router.get("/")
def get_messages():

    df = repo.get_messages()

    return {
        "rows": len(df),
        "columns": list(df.columns),
    }