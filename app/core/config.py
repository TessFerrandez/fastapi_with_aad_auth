from starlette.config import Config


config = Config(".env")

API_PREFIX: str = "/api"
VERSION: str = "0.1.0"
PROJECT_NAME: str = "FastAPI with AAD Authentication"
DEBUG: bool = config("DEBUG", cast=bool, default=False)

# Authentication
API_CLIENT_ID: str = config("API_CLIENT_ID", default="")
API_CLIENT_SECRET: str = config("API_CLIENT_SECRET", default="")
SWAGGER_UI_CLIENT_ID: str = config("SWAGGER_UI_CLIENT_ID", default="")
AAD_TENANT_ID: str = config("AAD_TENANT_ID", default="")

AAD_INSTANCE: str = config("AAD_INSTANCE", default="https://login.microsoftonline.com")
API_AUDIENCE: str = config("API_AUDIENCE", default=f"api://{API_CLIENT_ID}")
