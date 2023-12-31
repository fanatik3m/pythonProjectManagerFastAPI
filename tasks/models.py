from datetime import datetime

from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, Boolean

from auth.models import User
from database import Base
from projects.models import Project


class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    title = Column(String(64), nullable=False)
    description = Column(String)
    done = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    creator_id = Column(Integer, ForeignKey(User.id))
    executor_id = Column(Integer, ForeignKey(User.id))
    project_id = Column(Integer, ForeignKey(Project.id))