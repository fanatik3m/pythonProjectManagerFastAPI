from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from auth.models import Role
from auth.schemas import UserRead, UserCreate
from auth.users import fastapi_users, auth_backend
from database import get_async_session

from projects.router import router as router_projects
from schemas import RoleCreate
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


@app.post('/role')
async def add_role(data: RoleCreate, session: AsyncSession = Depends(get_async_session)):
    try:
        if data.password != '8372847382dhjsjfhsdkf7sd7fsfe4j3w8wfdsfhklslkjk':
            raise HTTPException(status_code=401)

        stmt = insert(Role).values(id=data.id, name=data.name)
        await session.execute(stmt)
        await session.commit()
        return {
            'status': 'ok',
            'details': {},
            'data': {}
        }
    except Exception as ex:
        raise HTTPException(status_code=500, detail={
            'status': 'error',
            'details': {'msg': str(ex)},
            'data': {}
        })