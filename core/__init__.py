from dotenv import dotenv_values
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from fastapi.staticfiles import StaticFiles

from .router import router


def create_app():
    app = FastAPI()
    
    # mount static files
    app.mount("/static", StaticFiles(directory="static"), name="static")
    
    register_tortoise(
        app=app,
        db_url="postgres://postgres:1234@localhost:5432/ecommerce_db",
        modules={"models": ["core.models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
    # add routes
    app.include_router(router)

    return app
