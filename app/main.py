import uvicorn
from fastapi import FastAPI

from api.routes.api import router as api_router
from core.config import DEBUG, PROJECT_NAME, VERSION


def get_application() -> FastAPI:
    application = FastAPI(
        title=PROJECT_NAME,
        debug=DEBUG,
        version=VERSION
        )
    application.include_router(api_router)
    return application


app = get_application()


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
