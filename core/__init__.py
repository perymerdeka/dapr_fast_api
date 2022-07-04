from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from .router import router

def create_app():
    app = FastAPI()
    register_tortoise(
        app=app,
        db_url="postgres://postgres:1234@localhost:5432/ecommerce_db",
        modules={"models": ["core.models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
    app.include_router(router)

    return app
