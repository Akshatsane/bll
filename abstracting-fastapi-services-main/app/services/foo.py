from schemas.foo import UserResponse, Userbase
from utils.app_exceptions import AppException

from services.main import AppService, AppCRUD
from models.foo import User
from utils.service_result import ServiceResult


class FooService(AppService):
    def create_user(self, user: UserResponse) -> ServiceResult:
        foo_user = FooCRUD(self.db).create_user(user)
        if not foo_user:
            return ServiceResult(AppException.FooCreateUser())
        return ServiceResult(foo_user)

    def get_user(self, id: int) -> ServiceResult:
        foo_user = FooCRUD(self.db).get_user(id)
        if not foo_user:
            return ServiceResult(AppException.FooGetUser({"id": id}))
        return ServiceResult(foo_user)

class FooCRUD(AppCRUD):
    def create_user(self, user: UserResponse) -> UserResponse:
        foo_user= UserResponse(id = user.id, username=user.username, email=user.email)
        self.db.add(foo_user)
        self.db.commit()
        self.db.refresh(foo_user)
        return foo_user

    def get_user(self, id: int) -> UserResponse:
        foo_user = self.db.query(UserResponse).filter(UserResponse.id == id).first()
        if foo_user:
            return foo_user
        return None
