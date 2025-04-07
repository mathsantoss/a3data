import datetime
from pydantic import BaseModel, ConfigDict, Field
from typing import Dict


class PredictionResponse(BaseModel):
    """
    Response model for Iris prediction result
    """
    species: str = Field(..., description="Predicted Iris species")
    probability: float = Field(..., ge=0, le=1, description="Probability of the predicted species")
    probabilities: Dict[str, float] = Field(..., description="Probability for each possible species")
    features: Dict[str, float] = Field(..., description="Input features used for prediction")
    model_name: str = Field(..., description="Nome do modelo utilizado")
    ConfigDict(arbitrary_types_allowed=True)

    class Config:
        json_schema_extra = {
            "example": {
                "species": "setosa",
                "probability": 0.98,
                "probabilities": {
                    "setosa": 0.98,
                    "versicolor": 0.01,
                    "virginica": 0.01
                },
                "features": {
                    "sepal_length": 5.1,
                    "sepal_width": 3.5,
                    "petal_length": 1.4,
                    "petal_width": 0.2
                }
            }
        }
