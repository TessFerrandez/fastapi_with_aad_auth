from starlette.config import Config


config = Config(".env")

API_PREFIX: str = "/api"
VERSION: str = "0.1.0"
PROJECT_NAME: str = "FastAPI with AAD Authentication"
DEBUG: bool = config("DEBUG", cast=bool, default=False)
