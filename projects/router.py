from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import insert, delete, select, text
from sqlalchemy.ext.asyncio import AsyncSession

from auth.models import User
from auth.users import current_user
from database import get_async_session
from projects.models import Project, ProjectHasUser
from projects.schemas import ProjectCreateSchema

router = APIRouter(
    prefix='/projects',
    tags=['Operations with projects']
)


@router.get('')
async def check_all_projects(page: int, session: AsyncSession = Depends(get_async_session)):
    try:
        offset = (page - 1) * 10
        query = select(Project).limit(10).offset(offset)
        result = await session.execute(query)
        return result.scalars().all()
    except Exception as ex:
        raise HTTPException(status_code=500, detail={
            'status': 'error',
            'details': {'msg': str(ex)},
            'data': {}
        })


@router.post('')
async def create_project(data: ProjectCreateSchema, session: AsyncSession = Depends(get_async_session),
                         user: User = Depends(current_user)):
    try:
        stmt = insert(Project).values(title=data.title, description=data.description, creator_id=user.id)
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


@router.post('/{project_id}/{user_id}')
async def add_users_to_project(project_id: int, user_id: int, session: AsyncSession = Depends(get_async_session), user: User = Depends(current_user)):
    try:
        query = select(Project).where(Project.id == project_id).where(Project.creator_id == user.id)
        result = await session.execute(query)
        if not len(result.all()):
            raise HTTPException(status_code=403, detail={
                'status': 'error',
                'details': {'msg': 'Forbidden'},
                'data': {}
            })

        stmt = insert(ProjectHasUser).values(user_id=user_id, project_id=project_id)
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


@router.delete('/{project_id}/{user_id}', dependencies=[Depends(current_user)])
async def delete_user_from_project(project_id: int, user_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Project).where(Project.id == project_id).where(Project.creator_id == user.id)
        result = await session.execute(query)
        if not len(result.all()):
            raise HTTPException(status_code=403, detail={
                'status': 'error',
                'details': {'msg': 'Forbidden'},
                'data': {}
            })

        stmt = delete(ProjectHasUser).where(user_id=user_id, project_id=project_id)
        await session.execute(stmt)
        await session.commit()
    except Exception as ex:
        raise HTTPException(status_code=500, detail={
            'status': 'error',
            'details': {'msg': str(ex)},
            'data': {}
        })


@router.get('')
async def check_self_projects(page: int, session: AsyncSession = Depends(get_async_session), user: User = Depends(current_user)):
    try:
        offset = (page - 1) * 10
        query = select(Project).where(Project.creator_id == user.id).limit(10).offset(offset)
        result = await session.execute(query)
        return result.scalars().all()
    except Exception as ex:
        raise HTTPException(status_code=500, detail={
            'status': 'error',
            'details': {'msg': str(ex)},
            'data': {}
        })