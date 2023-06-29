from datetime import datetime

from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey

from auth.models import User
from database import Base


class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True)
    title = Column(String(64), nullable=False)
    description = Column(String)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    creator_id = Column(Integer, ForeignKey(User.id))


class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    title = Column(String(64), nullable=False)
    description = Column(String)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    creator_id = Column(Integer, ForeignKey(User.id))
    executor_id = Column(Integer, ForeignKey(User.id))


class ProjectHasUser(Base):
    __tablename__ = 'project_has_user'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    project_id = Column(Integer, ForeignKey(Project.id))