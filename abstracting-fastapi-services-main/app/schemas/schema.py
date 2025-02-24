from pydantic import BaseModel
from typing import Optional, List


class Userbase(BaseModel):
    username: str
    email: str

class Userpass(Userbase):
    pass
    
class UserResponse(Userbase):
    id: int
    class Config:
        from_attributes = True

#class Todobase(BaseModel):
#    title: str
#    description: str

#class TodoCreate(Todobase):
#    user_id: int
    
#class TodoResponse(Todobase):
#    id: str
#    user_id: int
#    class Config: 
#        from_attributes = True


