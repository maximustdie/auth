from fastapi import APIRouter

user_router = APIRouter(tags=["auth"])


@user_router.post("/register")
async def register_user():
    return {"result": "user register"}


@user_router.post("/auth")
async def register_user():
    return {"result": "user auth"}


@user_router.post("/refresh")
async def register_user():
    return {"result": "token refresh"}
