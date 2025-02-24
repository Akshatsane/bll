from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.service import FooService
from schemas.schema import UserResponse #TodoResponse, Todobase, TodoCreate 
from models.model import User # Todo

from utils.service_result import handle_result

from config.database import get_db

router = APIRouter(
    prefix="/foo",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.post("/user/", response_model=UserResponse)
async def create_user(id: UserResponse, db: get_db = Depends()):
    result = FooService(db).create_user(id)
    return handle_result(result)


@router.get("/user/{user_id}", response_model=UserResponse)
async def get_user(id: int, db: get_db = Depends()):
    result = FooService(db).get_user(id)
    return handle_result(result)


#@router.post("/todos/", response_model = TodoCreate)
#async def create_todo(todo: TodoCreate, db: get_db = Depends()):
#    user_todo = db.query(User).filter(User.id == todo.user_id).first()
#    if not user_todo:
#        raise HTTPException(status_code=404, detail="User not found")
#    db_todo = Todo(**todo.dict())
#    db.add(db_todo)
#    db.commit()
#    db.refresh(db_todo)
#    return db_todo

#@router.get("/todos/{user_id}/todos", response_model = List[TodoResponse])
#async def get_user_todos(id: int, db: get_db = Depends()):
#    find_user_todos = db.query(User).filter(User.id == id).first()
#    if not find_user_todos:
#        raise HTTPException(status_code=404, detail="User not found")
#    
#    return handle_result(find_user_todos)