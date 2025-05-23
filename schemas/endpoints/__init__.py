from fastapi import APIRouter

from schemas.endpoints.auth import router as auth_router
from schemas.endpoints.chat import router as chat_router
from schemas.endpoints.user import router as user_router

routers = APIRouter()

api_routers = APIRouter(prefix="/api")
api_routers.include_router(user_router, tags=["User"])
api_routers.include_router(auth_router, tags=["Auth"])
api_routers.include_router(chat_router, tags=["Chat"])

routers.include_router(api_routers)
