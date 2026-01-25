from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from ..database import get_db
from ..schemas.todo import Todo, TodoCreate, TodoUpdate
from ..crud import todo as crud_todo

router = APIRouter()

@router.get("/", response_model=List[Todo])
async def read_todos(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    return await crud_todo.get_todos(db, skip=skip, limit=limit)

@router.post("/", response_model=Todo)
async def create_todo(todo: TodoCreate, db: AsyncSession = Depends(get_db)):
    return await crud_todo.create_todo(db=db, todo=todo)

@router.get("/{todo_id}", response_model=Todo)
async def read_todo(todo_id: int, db: AsyncSession = Depends(get_db)):
    db_todo = await crud_todo.get_todo(db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

@router.put("/{todo_id}", response_model=Todo)
async def update_todo(todo_id: int, todo: TodoUpdate, db: AsyncSession = Depends(get_db)):
    return await crud_todo.update_todo(db=db, todo_id=todo_id, todo=todo)

@router.delete("/{todo_id}")
async def delete_todo(todo_id: int, db: AsyncSession = Depends(get_db)):
    await crud_todo.delete_todo(db=db, todo_id=todo_id)
    return {"status": "success"}
