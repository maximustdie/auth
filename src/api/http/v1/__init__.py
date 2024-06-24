from fastapi import APIRouter

from api.http.v1 import auth

v1_router = APIRouter(prefix="/v1")

v1_router.include_router(auth.user_router)

