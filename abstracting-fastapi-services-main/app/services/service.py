from schemas.schema import UserResponse #TodoCreate, TodoResponse
from utils.app_exceptions import AppException
from services.main import AppService, AppCRUD
from models.model import User # Todo
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
    
#    def create_todo(self, todo: TodoCreate) -> ServiceResult:
#        foo_todo = FooCRUD(self.db).create_todo(todo)
#        if not foo_todo:
#            return ServiceResult(AppException.FooCreateTodo())
#        return ServiceResult(foo_todo) 
    
#    def get_todo(self, user_id: int) ->ServiceResult:
#        foo_todo = FooCRUD(self.db).get_todo(id)
#        if not foo_todo:
#            return ServiceResult(AppException.FooGetTodo({"user_id" = user_id}))
#        return ServiceResult(foo_todo)
    

class FooCRUD(AppCRUD):
    def create_user(self, user: UserResponse) -> UserResponse:
        foo_user= User(id = user.id, username=user.username, email=user.email)
        self.db.add(foo_user)
        self.db.commit()
        self.db.refresh(foo_user)
        return foo_user

    def get_user(self, id: int) -> UserResponse:
        foo_user = self.db.query(User).filter(User.id == id).first()
        if foo_user:
            return foo_user
        return None
    
#    def create_todo(self, todo: TodoCreate) -> TodoCreate:
#        foo_todo = Todo(id = todo.user_id, title = todo.title, description = todo.description)
#        self.db.add(foo_todo)
#        self.db.commit()
#        self.db.refresh(foo_todo)
#        return foo_todo

#    def get_todo(self, id: int) -> TodoResponse:
#       foo_todo

