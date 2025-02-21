from sqlalchemy import  Column, Integer, String
from config.database import Base



class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True, index = True)
    username = Column(String(100), nullable  = False)
    email = Column(String(255), nullable = False)




