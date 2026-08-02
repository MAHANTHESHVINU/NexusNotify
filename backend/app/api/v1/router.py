from fastapi import APIRouter

from app.api.v1.routes import (
    context,
    debug,
    features,
)

router = APIRouter()

router.include_router(debug.router)
router.include_router(context.router)
router.include_router(features.router)