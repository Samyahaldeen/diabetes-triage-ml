from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Diabetes Triage ML Service"
    model_path: str = "artifacts/model.pkl"
    model_version_path: str = "artifacts/version.txt"
    api_port: int = 8000

settings = Settings()
