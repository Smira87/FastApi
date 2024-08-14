from fastapi import APIRouter, Depends
from schemas import STaskAdd, STaskGet
from typing import Optional, Annotated
from repository import TaskRepository

router = APIRouter(
    prefix = "/tasks",
    tags = ["Tasks"],
)
@router.post("")
async def add_task(
        task: Annotated[STaskAdd, Depends()]
):
    task_id = await TaskRepository.add_one(task)
    return {"OK": True, "task_id": task_id}

@router.get("")
async def get_tasks():
    tasks = await TaskRepository.find_all()
    return {"tasks": tasks}