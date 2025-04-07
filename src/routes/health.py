import logging

from datetime import datetime
from fastapi import APIRouter, HTTPException
from src.dataclass.v1.health_response import HealthResponse
from src.utils.logger import setup_logging


router = APIRouter()

# Setup logging
setup_logging()
logger = logging.getLogger(__name__)


@router.get("/")#, response_model=HealthResponse)
async def health():
    """
    Health check endpoint
    """
    try:

        model_version = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return {"status": "healthy", "model_version": model_version}
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        raise HTTPException(status_code=503, detail=f"Service unavailable: {str(e)}")
