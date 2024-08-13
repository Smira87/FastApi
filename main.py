from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional, Annotated
from contextlib import asynccontextmanager
from database import create_tables, delete_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("DB cleared")
    await create_tables()
    print("DB created")
    yield
    print("Shutting down")

app = FastAPI(lifespan=lifespan)

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