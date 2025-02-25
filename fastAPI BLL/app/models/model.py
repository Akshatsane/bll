from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base



class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True, index = True)
    username = Column(String(100), nullable  = False)
    email = Column(String(255), nullable = False)

    todos = relationship("Todo", back_populates="owner")

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key = True, index = True)
    title = Column(String(100), index = True)
    description = Column(String(500), index = True)
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates = "todos")




