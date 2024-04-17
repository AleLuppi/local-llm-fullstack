from fastapi import APIRouter, status
from .models import HealthCheck

# Init router
router = APIRouter()


@router.get("/health", status_code=status.HTTP_200_OK, response_model=HealthCheck)
def get_health() -> HealthCheck:
    """
    Perform a health check.

    Endpoint to perform a health check. Other services which rely on proper
    functioning of the API service will not deploy if this endpoint returns
    any other HTTP status code except 200 (OK).

    :return: response with health status.
    """
    return HealthCheck(status="OK")
