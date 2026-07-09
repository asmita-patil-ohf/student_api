from pydantic import BaseModel, Field, EmailStr
from sqlalchemy import Column, Integer, String
from database import Base


class Student(Base):
    __tablename__ = "students"

    std_id = Column(Integer, primary_key=True)
    name = Column(String(50))
    roll_no = Column(Integer)
    grade = Column(String(5))


class Student(BaseModel):
    std_id:int = Field(
        gt = 0
    )
    name:str = Field(
        min_length=2,
        max_length=50
    )
    roll_no:int = Field(
        gt=0
    )
    grade:str = Field(
        min_length=1,
        max_length=1
    )
    email: EmailStr
   