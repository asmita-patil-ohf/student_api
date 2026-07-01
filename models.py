from pydantic import BaseModel, Field, EmailStr

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
   