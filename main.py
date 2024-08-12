from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional, Annotated

app = FastAPI()

class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None

class STaskGet(STaskAdd):
    id: int

tasks = []
@app.post("/tasks")
async def add_task(
        task: Annotated[STaskAdd, Depends()]
):
    tasks.append(task)
    return {"OK": True}

# @app.get('/home')
# def get_tasks():
#     task = Task(name = "Learn Python")
#     return {"data": task}