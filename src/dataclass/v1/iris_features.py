from pydantic import BaseModel, Field

class IrisFeatures(BaseModel):
    """
    Estrutura de entrada para inferência do modelo de classificação Iris.
    """
    sepal_length: float = Field(..., gt=0, description="Comprimento da sépala em cm")
    sepal_width: float = Field(..., gt=0, description="Largura da sépala em cm")
    petal_length: float = Field(..., gt=0, description="Comprimento da pétala em cm")
    petal_width: float = Field(..., gt=0, description="Largura da pétala em cm")

    class Config:
        json_schema_extra = {
            "example": {
                "sepal_length": 5.1,
                "sepal_width": 3.5,
                "petal_length": 1.4,
                "petal_width": 0.2
            }
        }
