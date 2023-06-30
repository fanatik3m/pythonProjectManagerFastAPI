from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str
    description: str
    executor_id: int
    project_id: int