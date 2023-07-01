from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import insert, delete, select, text
from sqlalchemy.ext.asyncio import AsyncSession

from auth.models import User
from auth.users import current_user
from database import get_async_session
from projects.models import Project, ProjectHasUser
from projects.schemas import ProjectCreateSchema
from repository import ProjectRepository

router = APIRouter(
    prefix='/projects',
    tags=['Operations with projects']
)

project_db_repository = ProjectRepository()


@router.get('/all')
async def check_all_projects(page: int, session: AsyncSession = Depends(get_async_session)):
    try:
        offset = (page - 1) * 10
        data = await project_db_repository.db_check_all_projects(offset=offset, session=session)
        return {
            'status': 'ok',
            'details': {},
            'data': data
        }
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
        await project_db_repository.db_create_project(data=data, session=session, user=user)
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
async def add_users_to_project(project_id: int, user_id: int, session: AsyncSession = Depends(get_async_session),
                               user: User = Depends(current_user)):
    try:
        await project_db_repository.db_add_users_to_project(project_id=project_id, user_id=user_id, session=session,
                                                            user=user)
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


@router.delete('/{project_id}/{user_id}')
async def delete_user_from_project(project_id: int, user_id: int, session: AsyncSession = Depends(get_async_session),
                                   user: User = Depends(current_user)):
    try:
        await project_db_repository.db_delete_user_from_project(project_id=project_id, user_id=user_id, session=session,
                                                                user=user)
    except Exception as ex:
        raise HTTPException(status_code=500, detail={
            'status': 'error',
            'details': {'msg': str(ex)},
            'data': {}
        })


@router.get('')
async def check_self_projects(page: int, session: AsyncSession = Depends(get_async_session),
                              user: User = Depends(current_user)):
    try:
        offset = (page - 1) * 10
        data = await project_db_repository.db_check_self_projects(offset=offset, session=session, user=user)
        return {
            'status': 'ok',
            'details': {},
            'data': data
        }
    except Exception as ex:
        raise HTTPException(status_code=500, detail={
            'status': 'error',
            'details': {'msg': str(ex)},
            'data': {}
        })
