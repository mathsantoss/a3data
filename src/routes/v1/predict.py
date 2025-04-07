from datetime import datetime
import logging
import os
import pickle
import pandas as pd
import numpy as np

from fastapi import APIRouter, HTTPException
from src.dataclass.v1.prediction_response import  PredictionResponse
from src.dataclass.v1.iris_features import IrisFeatures

logger = logging.getLogger(__name__)
router = APIRouter()

# Caminhos dos artefatos
MODEL_PATH = "src/artefacts/iris_model.pickle"

# Variáveis globais para cache
_model = None
_metadata = None

def load_model():
    """
    Carrega o modelo e os metadados do disco (somente uma vez)
    """
    global _model, _metadata

    if _model is None or _metadata is None:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Arquivo do modelo não encontrado: {MODEL_PATH}")

        try:
            with open(MODEL_PATH, 'rb') as f:
                model_bundle = pickle.load(f)
                _model = model_bundle["model"]
                _metadata = model_bundle["metadata"]

            logger.info("Modelo carregado com sucesso")
        except Exception as e:
            logger.error(f"Erro ao carregar modelo: {e}")
            raise

    return _model, _metadata


@router.post(
    "/predict",
    tags=["a3data"],
    summary="Predict model",
    description="This endpoint is used to make inference requests",
    response_description="inference handler",
)
async def predict_species(features: IrisFeatures):
    """
    Prediz a espécie da flor Íris com base nas medidas fornecidas.
    
    Parameters
    ----------
    features : IrisFeatures
        Medidas da flor (sépalas e pétalas)

    Returns
    -------
    dict
        Resultado com espécie prevista e probabilidades
    """
    # request_start_time = datetime.now(datetime.timezone.utc)
    try:
        model, metadata = load_model()

        # Transformar input em DataFrame
        features_dict = features.model_dump()
        feature_names = metadata["feature_names"]

        df = pd.DataFrame([[features_dict[name] for name in feature_names]], columns=feature_names)
        logger.info(f"Realizando predição para: {features_dict}")

        # Predição e probabilidades
        species_pred = model.predict(df)[0]
        probabilities = model.predict_proba(df)[0]
        class_names = metadata["target_names"]

        prob_dict = {name: float(prob) for name, prob in zip(class_names, probabilities)}
        predicted_prob = float(probabilities[np.argmax(probabilities)])


        return PredictionResponse(
            species=class_names[species_pred],
            probability=predicted_prob,
            probabilities=prob_dict,
            features=features_dict,
            model_name=metadata.get("model_type", "UnknownModel"),

        )

    except Exception as e:
        logger.error(f"Erro ao realizar predição: {e}")
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")
