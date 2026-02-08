from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class TaskBase(SQLModel):
    title: str = Field(min_length=1, max_length=255)
    description: Optional[str] = Field(default=None)
    user_id: str = Field(index=True)  # Using string for user_id as it could be UUID
    completed: bool = Field(default=False)

print("TaskBase defined successfully")

class Task(TaskBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

print("Task defined successfully")