from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dependencies import get_db
from models import Student
from schemas import CreateStudent

from utils import search, read_students, write_students


import json

router = APIRouter()

@router.get("/")
def all_students():
    return read_students()

@router.get("/students/{student_id}", response_model=CreateStudent)
def id_student(student_id:int)->CreateStudent:
        students = read_students()
        get_index=search(student_id)    
        if get_index == -1: 
            raise HTTPException(status_code=404, detail="Student not found!")
        return students[get_index]
    

@router.post("/students") 
def create_student(student: CreateStudent, db: Session = Depends(get_db)):
        db_student = Student(**student.model_dump())
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student

@router.put("/students/{student_id}")
def update_student(student_id:int,student:CreateStudent, db: Session = Depends(get_db)):
        db_student = Student(**student.model_dump())
        db.update(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student


@router.delete("/students/{student_id}")
def delete_student(student_id:int):
        del_index=search(student_id)
        if del_index == -1: 
            raise HTTPException(status_code=404, detail="Student not found!")
        students = read_students()
        del students[del_index]
        write_students(students)
        return {
            "message":"Student deleted successfully"
        }

    
    
    
@router.post("/students")
def create_student(student:CreateStudent):
    verify_stud=search(student.std_id)
    if verify_stud != -1: 
        raise HTTPException(status_code=409, detail="Student already added!") 
    students = read_students()
    students.append(student.model_dump())
    write_students(students)
    return {
            "message":"Student added successfully"
        }
    
    
@router.put("/students/{student_id}")
def update_student(student_id:int,student:CreateStudent):
        duplicate_index = search(student.std_id)
        if duplicate_index != -1 and student.std_id != student_id: 
            raise HTTPException(status_code=409, detail="Student already added!") 
        update_index=search(student_id)
        if update_index == -1: 
            raise HTTPException(status_code=404, detail="Student not found!")
        students = read_students()
        student=student.model_dump()
        students[update_index]=student
        write_students(students)
        return {
            "message":"Student updated successfully"
        }