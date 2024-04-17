from pydantic import BaseModel


class HealthCheck(BaseModel):
    """
    Response model when performing a health check.
    """
    status: str = "OK"
