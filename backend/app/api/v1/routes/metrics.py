from fastapi import APIRouter, HTTPException

from app.services.analytics.metrics_service import MetricsService

router = APIRouter(
    prefix="/metrics",
    tags=["Metrics"],
)

service = MetricsService()


@router.get("/")
def get_metrics():

    try:
        return service.get_metrics()

    except FileNotFoundError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )