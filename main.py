from fastapi import FastAPI

from auth.schemas import UserRead, UserCreate
from auth.users import fastapi_users, auth_backend

app = FastAPI(
    title='Project Manager'
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"]
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
