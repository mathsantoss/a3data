from pydantic import BaseModel, Field
from typing import Dict


class HealthResponse(BaseModel):
    """
    Pydantic model for health check response
    """

    status: str = Field(..., description="API status")
