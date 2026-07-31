from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dependencies import get_db
from models import Student
from schemas import CreateStudent, StudentResponse

from typing import List

router = APIRouter()

@router.get("/", response_model=List[StudentResponse])
def get_all_studnets(db:Session = Depends(get_db)):
    db_students = (
            db.query(Student)
            .all()
        )
    return db_students

@router.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id, db:Session = Depends(get_db)):
        db_student = (
            db.query(Student)
            .filter(Student.id == student_id)
            .first()
        )
        if db_student is None:
            raise HTTPException (
                status_code=404,
                detail="Student not found"
            )
        return db_student

@router.post("/students") 
def create_student(student: CreateStudent, db: Session = Depends(get_db)):
        db_student = Student(**student.model_dump())
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return {
            "message": "Student added successfully"
        }

@router.put("/students/{student_id}")
def update_student(student_id:int,student:CreateStudent, db: Session = Depends(get_db)):
        db_student = (
            db.query(Student)
            .filter(Student.id == student_id)
            .first()
        )
        if db_student is None:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )
        db_student.name= student.name
        db_student.roll_no= student.roll_no
        db_student.email= student.email
        db_student.grade= student.grade
        db.commit()
        db.refresh(db_student)
        return {
            "message": "Student updated successfully"
        }

@router.delete("/students/{student_id}")
def delete_student(student_id:int, db: Session = Depends(get_db)):
    db_student = (
        db.query(Student)
        .filter(Student.id == student_id)
        .first()
    )
    if db_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
    db.delete(db_student)
    db.commit()
    return {
            "message": "Student deleted successfully"
        }
