from fastapi import APIRouter, Depends

from services.foo import FooService
from schemas.foo import UserResponse


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
