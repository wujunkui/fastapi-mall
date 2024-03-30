from fastapi import APIRouter
from apis.routers import upload, user, item

api_router = APIRouter()

api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(upload.router, prefix="/upload", tags=["upload"])
api_router.include_router(item.router, prefix="/mall", tags=["item"])
