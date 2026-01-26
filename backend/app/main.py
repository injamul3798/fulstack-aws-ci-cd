from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.todo import router as todo_router
from .database import engine
from .models.todo import Base

app = FastAPI(title="To-Do App API test01 final ")

# CORS middleware for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        # Create tables if they don't exist
        await conn.run_sync(Base.metadata.create_all)

app.include_router(todo_router, prefix="/api/todos", tags=["todos"])

@app.get("/")
async def root():
    return {"message": "Welcome to the To-Do App API"}
