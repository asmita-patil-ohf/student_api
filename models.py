from sqlalchemy import Column, Integer, String
from database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True,  autoincrement=True)
    name = Column(String(50))
    roll_no = Column(Integer)
    grade = Column(String(5))


