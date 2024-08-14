from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("DB cleared")
    await create_tables()
    print("DB created")
    yield
    print("Shutting down")

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
