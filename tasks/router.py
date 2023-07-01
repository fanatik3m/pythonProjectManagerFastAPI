from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import insert, update, select
from sqlalchemy.ext.asyncio import AsyncSession

from auth.models import User
from auth.users import current_user
from database import get_async_session
from projects.models import Project, ProjectHasUser
from repository import TaskRepository
from tasks.models import Task
from tasks.schemas import TaskCreate

router = APIRouter(
    prefix='/projects/tasks',
    tags=['Operations with tasks']
)

task_db_repository = TaskRepository()


@router.post('')
async def add_task(task: TaskCreate, session: AsyncSession = Depends(get_async_session),
                   user: User = Depends(current_user)):
    try:
        await task_db_repository.db_add_task(task=task, session=session, user=user)
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


@router.put('/{task_id}')
async def mark_task_done(task_id: int, session: AsyncSession = Depends(get_async_session),
                         user: User = Depends(current_user)):
    try:
        await task_db_repository.db_mark_task_done(task_id=task_id, session=session, user=user)
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


@router.get('')
async def check_self_tasks(page: int, session: AsyncSession = Depends(get_async_session),
                           user: User = Depends(current_user)):
    try:
        offset = (page - 1) * 10
        data = await task_db_repository.db_check_self_tasks(offset=offset, session=session, user=user)
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


@router.get('/completed')
async def check_self_completed_tasks(page: int, session: AsyncSession = Depends(get_async_session),
                                     user: User = Depends(current_user)):
    try:
        offset = (page - 1) * 10
        data = await task_db_repository.db_check_self_completed_tasks(offset=offset, session=session, user=user)
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


@router.get('/uncompleted')
async def check_self_uncompleted_tasks(page: int, session: AsyncSession = Depends(get_async_session),
                                       user: User = Depends(current_user)):
    try:
        offset = (page - 1) * 10
        data = await task_db_repository.check_self_uncompleted_tasks(offset=offset, session=session, user=user)
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
