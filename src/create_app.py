import os
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes.health import router as health_router
from src.routes.v1.predict import router as predict_router

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def create_app() -> FastAPI:
    """Creates app with the FastAPI framework.

    Returns:
        FastAPI: FastAPI App
    """
    # Tente importar a versão, se não conseguir, defina uma versão padrão
    try:
        from _version import __version__
    except ImportError:
        __version__ = "0.1.0"

    app = FastAPI(
        title="Iris Classifier API",
        version=__version__,
        summary="API para classificação de flores de íris",
        description="Esta API classifica espécies de íris com base em medidas de sépalas e pétalas",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    # Adicionar middleware CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include routers
    app.include_router(health_router)
    app.include_router(predict_router, prefix="/v1")

    logger.info("Application startup complete")
    return app