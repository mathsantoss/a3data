from src.create_app import create_app

"""
  Entry point to FastAPI
"""

application = create_app()


if __name__ == "__main__":
    application.run(application, host="0.0.0.0", port=8000, reload=True)
