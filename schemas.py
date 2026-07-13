from pydantic import BaseModel, Field, EmailStr

class CreateStudent(BaseModel):
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
   