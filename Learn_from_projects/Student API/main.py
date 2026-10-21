
from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import init_db, close_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    await close_db()


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Backend is running"}

import uvicorn

if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)
    