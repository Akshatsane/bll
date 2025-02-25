from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from services.service import FooService
from schemas.schema import UserResponse, TodoResponse, TodoCreate 
from models.model import User

from utils.service_result import handle_result

from config.database import get_db

router = APIRouter(
    prefix="/foo",
    responses={404: {"description": "Not found"}},
)


@router.post("/user/", response_model=UserResponse, tags= ["users"])
async def create_user(id: UserResponse, db: Session = Depends(get_db)):
    result = FooService(db).create_user(id)
    return handle_result(result)


@router.get("/user/{user_id}", response_model=UserResponse, tags= ["users"])
async def get_user(id: int, db: Session = Depends(get_db)):
    result = FooService(db).get_user(id)
    return handle_result(result)

@router.post("/todos/", response_model=TodoResponse, tags= ["todos"])
async def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    user_todo = db.query(User).filter(User.id == todo.user_id).first()
    result = FooService(db).create_todo(todo)
    return handle_result(result)

@router.get("/todos/{user_id}/todos", response_model = List[TodoResponse], tags= ["todos"])
async def get_user_todos(user_id: int, db: Session = Depends(get_db)):
    result =  FooService(db).get_todo(user_id)
    return handle_result(result)



