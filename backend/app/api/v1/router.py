from fastapi import APIRouter
from app.api.v1.routes import metrics
from app.api.v1.routes import messages
from app.api.v1.routes import predictions
from app.api.v1.routes import prediction_details


from app.api.v1.routes import (
    context,
    debug,
    features,
)

router = APIRouter()

router.include_router(debug.router)
router.include_router(context.router)
router.include_router(features.router)
router.include_router(messages.router)
router.include_router(metrics.router)
router.include_router(predictions.router)
router.include_router(prediction_details.router)