from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from apis.main import api_router

app = FastAPI()

app.include_router(api_router, prefix="/api")

app.mount("/static", StaticFiles(directory="static"), name="static")
