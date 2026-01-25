from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from ..models.todo import TodoItem
from ..schemas.todo import TodoCreate, TodoUpdate

async def get_todos(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(TodoItem).offset(skip).limit(limit))
    return result.scalars().all()

async def get_todo(db: AsyncSession, todo_id: int):
    result = await db.execute(select(TodoItem).where(TodoItem.id == todo_id))
    return result.scalar_one_or_none()

async def create_todo(db: AsyncSession, todo: TodoCreate):
    db_todo = TodoItem(**todo.dict())
    db.add(db_todo)
    await db.commit()
    await db.refresh(db_todo)
    return db_todo

async def update_todo(db: AsyncSession, todo_id: int, todo: TodoUpdate):
    query = update(TodoItem).where(TodoItem.id == todo_id).values(**todo.dict(exclude_unset=True))
    await db.execute(query)
    await db.commit()
    return await get_todo(db, todo_id)

async def delete_todo(db: AsyncSession, todo_id: int):
    await db.execute(delete(TodoItem).where(TodoItem.id == todo_id))
    await db.commit()
    return True
