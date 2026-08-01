from fastapi import APIRouter

from app.api.v1.routes import messages

router = APIRouter()

router.include_router(messages.router)