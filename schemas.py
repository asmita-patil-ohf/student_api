from pydantic import BaseModel, Field, EmailStr, ConfigDict

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


class StudentResponse(BaseModel):
    id: int
    name: str
    roll_no: int
    grade: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)
   