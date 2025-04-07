# """
# Script para treinamento do classificador Iris e exportação em formato pickle
# """

# import os
# import pickle
# import numpy as np
# import pandas as pd
# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.pipeline import Pipeline
# from sklearn.metrics import accuracy_score, classification_report

# # Cria diretório para os modelos, se não existir
# os.makedirs('models', exist_ok=True)

# # Carrega os dados Iris
# print("Carregando dataset Iris...")
# iris = load_iris()
# X = pd.DataFrame(iris.data, columns=iris.feature_names)
# y = iris.target

# # Renomeia colunas para o padrão da API
# X.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
# target_names = iris.target_names

# # Divide em conjuntos de treino e teste (80% treino, 20% teste)
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42, stratify=y
# )
# print(f"Dados divididos: treino={X_train.shape}, teste={X_test.shape}")

# # Cria pipeline com preprocessamento e modelo
# print("Criando pipeline de modelo...")
# pipeline = Pipeline([
#     ('scaler', StandardScaler()),
#     ('model', RandomForestClassifier(n_estimators=100, random_state=42))
# ])

# # Treina o modelo
# print("Treinando modelo...")
# pipeline.fit(X_train, y_train)

# # Avalia o modelo
# y_pred = pipeline.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)
# print(f"\nAcurácia do modelo: {accuracy:.4f}")
# print("\nRelatório de classificação:")
# print(classification_report(y_test, y_pred, target_names=target_names))

# # Cria estrutura de metadados
# metadata = {
#     "feature_names": X.columns.tolist(),
#     "target_names": target_names.tolist(),
#     "model_type": "RandomForest",
#     "model_params": {"n_estimators": 100, "random_state": 42},
#     "accuracy": float(accuracy)
# }

# # Salva o modelo em formato pickle
# model_path = "src/arterfacts/iris_model.pickle"
# print(f"Salvando modelo em: {model_path}")
# with open(model_path, 'wb') as f:
#     pickle.dump(pipeline, f)

# # Salva os metadados em formato pickle
# metadata_path = "src/arterfacts/model_metadata.pickle"
# print(f"Salvando metadados em: {metadata_path}")
# with open(metadata_path, 'wb') as f:
#     pickle.dump(metadata, f)

# print("\nTreinamento concluído com sucesso!")
# print(f"Modelo salvo em: {model_path}")
# print(f"Metadados salvos em: {metadata_path}")

# train_model.py (deve estar dentro de src/projects ou src/projects/iris_classifier)

import os
import pickle
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report

# Diretório para armazenar modelos
MODEL_DIR = "src/artefacts"
os.makedirs(MODEL_DIR, exist_ok=True)

MODEL_PATH = os.path.join(MODEL_DIR, "iris_model.pickle")

def train_model():
    """Treina e salva um modelo RandomForest para classificação da base Iris."""
    # Carregar dataset Iris
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=["sepal_length", "sepal_width", "petal_length", "petal_width"])
    y = iris.target

    # Separar dados de treino e teste
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Criar pipeline de modelo
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('model', RandomForestClassifier(n_estimators=100, random_state=42))
    ])

    # Treinar modelo
    pipeline.fit(X_train, y_train)

    # Avaliação
    y_pred = pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Acurácia do modelo: {accuracy:.4f}")
    print(classification_report(y_test, y_pred, target_names=iris.target_names))

    # Criar estrutura de modelo com metadados
    model_data = {
        "model": pipeline,
        "metadata": {
            "feature_names": X.columns.tolist(),
            "target_names": iris.target_names.tolist(),
            "model_type": "RandomForest",
            "accuracy": float(accuracy)
        }
    }

    # Salvar tudo em um único arquivo pickle
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(model_data, f)

    print(f"Modelo e metadados salvos em: {MODEL_PATH}")

if __name__ == "__main__":
    train_model()
