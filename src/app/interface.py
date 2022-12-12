"""
    Appellation: interface
    Contributors: FL03 <jo3mccain@icloud.com> (https://gitlab.com/FL03)
    Description:
        ... Summary ...
"""
import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from tortoise.contrib.fastapi import register_tortoise

from synapse import api, core

app: FastAPI = FastAPI()
session: core.Session = core.session()
settings: core.Settings = session.settings

@app.on_event("startup")
async def startup():
    print("Starting the application...")

    print("View the server locally at http://localhost:{}".format(settings.server.port))


@app.get("/")
async def homepage() -> RedirectResponse:
    return RedirectResponse("/docs")


@app.on_event("shutdown")
async def shutdown():
    print("Terminating the application...")


app.include_router(router=api.api_router)

register_tortoise(
    app,
    add_exception_handlers=True,
    db_url=settings.db_uri,
    generate_schemas=True,
    modules=dict(models=['app.data.models'])
)


def run(host: str = "0.0.0.0", port=8080, reload=True):
    uvicorn.run("app.interface:app", host=host, port=port, reload=reload)


if __name__ == '__main__':
    run()
