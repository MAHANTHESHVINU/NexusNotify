from dataclasses import asdict

from fastapi import APIRouter, HTTPException

from app.services.context_builder import ContextBuilder

router = APIRouter(
    prefix="/context",
    tags=["Context"],
)

builder = ContextBuilder()


@router.get("/{message_id}")
def get_context(message_id: str):

    context = builder.build(message_id)

    if context is None:
        raise HTTPException(status_code=404, detail="Message not found")

    return asdict(context)