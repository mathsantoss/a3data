# Iris Classifier API

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Framework](https://img.shields.io/badge/Framework-FastAPI-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) <!-- Adicione um arquivo LICENSE se desejar -->

API RESTful para classificação de espécies de flores de Íris usando um modelo de Machine Learning.

## Descrição

Esta API recebe as medidas (comprimento e largura) das sépalas e pétalas de uma flor de Íris e retorna a classificação da espécie (Setosa, Versicolor ou Virginica) juntamente com as probabilidades associadas, utilizando um modelo pré-treinado (RandomForestClassifier).

## Features

*   **Classificação de Íris:** Endpoint principal `/v1/predict` para obter predições.
*   **Verificação de Saúde:** Endpoint `/health` para monitoramento básico.
*   **Validação de Dados:** Uso de Pydantic para garantir que os dados de entrada e saída estejam no formato correto.
*   **Documentação Interativa:** Acesso fácil à documentação da API via Swagger UI (`/docs`) e ReDoc (`/redoc`).
*   **Modelo Pré-treinado:** Utiliza um pipeline do Scikit-learn salvo em formato pickle.
*   **Desempenho:** Carregamento do modelo em cache na memória para respostas rápidas.
*   **Estrutura Modular:** Código organizado para facilitar a manutenção e extensão.

## Pré-requisitos

*   Python 3.8 ou superior
*   pip (gerenciador de pacotes Python)
*   Git (opcional, para clonar o repositório)

## Configuração e Instalação

1.  **Clone o Repositório (se aplicável):**
    ```bash
    git clone <url-do-repositorio>
    cd <nome-do-diretorio-do-projeto>
    ```

2.  **Crie e Ative um Ambiente Virtual (Recomendado):**
    ```bash
    conda create -n "a3data" python=3.12.* openjdk=8 -y
    ```

3.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

## Reproduzindo a Pipeline de Treinamento

A "pipeline" neste contexto refere-se ao processo de treinamento do modelo de classificação e salvamento do artefato (`.pickle`) utilizado pela API.

1.  **Execute o Script de Treinamento:**
    Navegue até o diretório raiz do projeto (onde `main.py` e a pasta `src` estão localizados) e execute o script `iris_model.py`:

    ```bash
    python src/iris_model.py
    ```

2.  **Verifique a Saída:**
    Este comando irá:
    *   Carregar o dataset Iris.
    *   Dividir os dados em treino e teste.
    *   Treinar um pipeline `StandardScaler` + `RandomForestClassifier`.
    *   Avaliar o modelo e imprimir a acurácia e o relatório de classificação no console.
    *   Criar o diretório `src/artefacts` (se não existir).
    *   Salvar o pipeline treinado junto com metadados no arquivo `src/artefacts/iris_model.pickle`.

    Este arquivo `iris_model.pickle` é o que a API carrega para fazer as predições. Você só precisa executar este passo se quiser retreinar o modelo ou se o arquivo `.pickle` não estiver presente.

## Iniciando a API

Após instalar as dependências e garantir que o arquivo `src/artefacts/iris_model.pickle` existe (seja por tê-lo no repositório ou por executar a pipeline de treinamento):

1.  **Inicie o Servidor Uvicorn:**
    No diretório raiz do projeto, execute o seguinte comando:

    ```bash
    uvicorn src.main:application
    ```

    *   `src.main:application`: Aponta para o objeto `application` (a instância FastAPI) dentro do arquivo `main.py`.
    *   `--host 0.0.0.0`: Torna a API acessível na sua rede local (use `127.0.0.1` para acesso apenas local).
    *   `--port 8000`: Define a porta em que a API será executada.
    *   `--reload`: (Opcional, para desenvolvimento) Reinicia o servidor automaticamente quando detecta alterações no código. Remova isso para produção.

2.  **Acesse a API:**
    A API estará disponível em `http://localhost:8000` (ou o IP da sua máquina na porta 8000).
    *   **Documentação Interativa (Swagger):** [http://localhost:8000/docs](http://localhost:8000/docs)
    *   **Documentação Alternativa (ReDoc):** [http://localhost:8000/redoc](http://localhost:8000/redoc)
    *   **Endpoint de Saúde:** [http://localhost:8000/health](http://localhost:8000/health)

## Usando a API - Exemplo de Predição

Você pode enviar uma requisição `POST` para o endpoint `/v1/predict` com os dados da flor no corpo da requisição em formato JSON.


**Exemplo usando `curl`:**

```bash
curl -X 'POST' \
  'http://localhost:8000/v1/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}'
```

## Roadmap

* Implementar docker
* Implementar https://kedro.org/
