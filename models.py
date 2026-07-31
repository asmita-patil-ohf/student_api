from sqlalchemy import Column, Integer, String
from database import Base


class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    roll_no = Column(Integer, nullable=False)
    grade = Column(String(2), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50),unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    
    