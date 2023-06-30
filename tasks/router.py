from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import insert, update, select
from sqlalchemy.ext.asyncio import AsyncSession

from auth.models import User
from auth.users import current_user
from database import get_async_session
from projects.models import Project
from tasks.models import Task
from tasks.schemas import TaskCreate

router = APIRouter(
    prefix='/projects/tasks',
    tags=['Operations with tasks']
)


@router.post('')
async def add_task(task: TaskCreate, session: AsyncSession = Depends(get_async_session),
                   user: User = Depends(current_user)):
    try:
        # query = select(Project).where(Project.id == task.project_id).where(Project.creator_id == user.id)
        # result = await session.execute(query)
        # if not len(result.all()):
        #     raise HTTPException(status_code=403, detail={
        #         'status': 'error',
        #         'details': {'msg': 'Forbidden'},
        #         'data': {}
        #     })

        stmt = insert(Task).values(title=task.title, description=task.description, executor_id=task.executor_id,
                                   creator_id=user.id, project_id=task.project_id)
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


@router.put('/{task_id}')
async def mark_task_done(task_id: int, session: AsyncSession = Depends(get_async_session),
                         user: User = Depends(current_user)):
    try:
        stmt = update(Task).where(Task.id == task_id).where(Task.executor_id == user.id).values(done=True)
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


@router.get('')
async def check_self_tasks(page: int, session: AsyncSession = Depends(get_async_session), user: User = Depends(current_user)):
    try:
        offset = (page - 1) * 10
        query = select(Task).where(Task.executor_id == user.id).limit(10).offset(offset)
        result = await session.execute(query)
        return result.scalars().all()
    except Exception as ex:
        raise HTTPException(status_code=500, detail={
            'status': 'error',
            'details': {'msg': str(ex)},
            'data': {}
        })