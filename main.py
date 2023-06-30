from fastapi import FastAPI

from auth.schemas import UserRead, UserCreate
from auth.users import fastapi_users, auth_backend

from projects.router import router as router_projects
from tasks.router import router as router_tasks

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

app.include_router(router_projects)
app.include_router(router_tasks)
