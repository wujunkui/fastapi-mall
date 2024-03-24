from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from mall import user, upload

app = FastAPI()

app.include_router(user.router, prefix="/user", tags=["user"])
app.include_router(upload.router, prefix="/upload", tags=["upload"])

app.mount("/static", StaticFiles(directory="static"), name="static")
