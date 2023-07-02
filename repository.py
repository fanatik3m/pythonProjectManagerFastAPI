from fastapi import HTTPException
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from auth.models import User
from projects.models import Project, ProjectHasUser
from projects.schemas import ProjectCreateSchema
from tasks.schemas import TaskCreate
from tasks.models import Task
from utils import check_len


class ProjectRepository:
    async def db_check_all_projects(self, offset: int, session: AsyncSession):
        query = select(Project).limit(10).offset(offset)
        result = await session.execute(query)
        return result.scalars().all()

    async def db_create_project(self, data: ProjectCreateSchema, session: AsyncSession, user: User):
        stmt = insert(Project).values(title=data.title, description=data.description, creator_id=user.id)
        await session.execute(stmt)
        await session.commit()

    async def db_add_users_to_project(self, project_id: int, user_id: int, session: AsyncSession, user: User):
        query = select(Project).where(Project.id == project_id).where(Project.creator_id == user.id)
        result = await session.execute(query)
        check_len(result)

        stmt = insert(ProjectHasUser).values(user_id=user_id, project_id=project_id)
        await session.execute(stmt)
        await session.commit()

    async def db_delete_user_from_project(self, project_id: int, user_id: int, session: AsyncSession, user: User):
        query = select(Project).where(Project.id == project_id).where(Project.creator_id == user.id)
        result = await session.execute(query)
        check_len(result)

        stmt = delete(ProjectHasUser).where(ProjectHasUser.user_id == user_id).where(
            ProjectHasUser.project_id == project_id)
        await session.execute(stmt)
        await session.commit()

    async def db_check_self_projects(self, offset: int, session: AsyncSession, user: User):
        query = select(Project).where(Project.creator_id == user.id).limit(10).offset(offset)
        result = await session.execute(query)
        return result.scalars().all()


class TaskRepository:
    async def db_add_task(self, task: TaskCreate, session: AsyncSession, user: User):
        query = select(Project).where(Project.id == task.project_id).where(Project.creator_id == user.id)
        result = await session.execute(query)
        check_len(result)

        query = select(ProjectHasUser).where(ProjectHasUser.project_id == task.project_id).where(
            ProjectHasUser.user_id == task.executor_id)
        result = await session.execute(query)
        check_len(result)

        stmt = insert(Task).values(title=task.title, description=task.description, executor_id=task.executor_id,
                                   creator_id=user.id, project_id=task.project_id)
        await session.execute(stmt)
        await session.commit()

    async def db_mark_task_done(self, task_id: int, session: AsyncSession, user: User):
        stmt = update(Task).where(Task.id == task_id).where(Task.executor_id == user.id).values(done=True)
        await session.execute(stmt)
        await session.commit()

    async def db_check_self_tasks(self, offset: int, session: AsyncSession, user: User):
        query = select(Task).where(Task.executor_id == user.id).limit(10).offset(offset)
        result = await session.execute(query)
        return result.scalars().all()

    async def db_check_self_completed_tasks(self, offset: int, session: AsyncSession, user: User):
        query = select(Task).where(Task.executor_id == user.id).where(Task.done).limit(10).offset(offset)
        result = await session.execute(query)
        return result.scalars().all()

    async def check_self_uncompleted_tasks(self, offset: int, session: AsyncSession, user: User):
        query = select(Task).where(Task.executor_id == user.id).where(Task.done == False).limit(10).offset(offset)
        result = await session.execute(query)
        return result.scalars().all()
