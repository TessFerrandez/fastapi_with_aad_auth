import uvicorn
from fastapi import FastAPI

from api.routes.api import router as api_router
from core import config


def get_application() -> FastAPI:
    application = FastAPI(
        title=config.PROJECT_NAME,
        debug=config.DEBUG,
        version=config.VERSION,
        swagger_ui_oauth2_redirect_url='/oauth2-redirect',
        swagger_ui_init_oauth={
            "usePkceWithAuthorizationCodeGrant": True,
            "clientId": config.SWAGGER_UI_CLIENT_ID,
            "scopes": [f'api://{config.API_CLIENT_ID}/access_as_user']
        }
    )
    application.include_router(api_router)
    return application


app = get_application()


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
