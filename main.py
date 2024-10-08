from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from starlette.responses import RedirectResponse

from app.users import routes as users


app = FastAPI()


TORTOISE_ORM = {
    "connections": {"default": "sqlite://db.sqlite3"},
    "apps": {
        "models": {
            "models": ["app.users.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)

app.include_router(users.router, tags=["Users"], prefix="/api/users")

@app.get("/")
async def redirect_to_docs():
    return RedirectResponse(url="/docs")
