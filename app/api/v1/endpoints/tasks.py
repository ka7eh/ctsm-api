from typing import Any

from fastapi import APIRouter

from app.schemas import TaskSchema
from app.tasks import celery_app

router = APIRouter()


@router.get("/{task_id}", response_model=TaskSchema)
def get_task(task_id: str) -> Any:
    task = celery_app.AsyncResult(task_id)
    return TaskSchema(task_id=task.task_id, status=task.status, result=task.result)