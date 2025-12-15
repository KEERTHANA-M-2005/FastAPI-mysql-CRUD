from fastapi import APIRouter, HTTPException
from models.student_model import Student, StudentResponse
from services.student_service import *

router = APIRouter()

@router.post("/students")
def add_student(student: Student):
    create_student(student.dict())
    return {"message": "Student added successfully"}


@router.get("/students", response_model=list[StudentResponse])
def fetch_students():
    return get_all_students()


@router.get("/students/{id}", response_model=StudentResponse)
def fetch_student(id: int):
    student = get_student_by_id(id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@router.put("/students/{id}")
def modify_student(id: int, student: Student):
    if not get_student_by_id(id):
        raise HTTPException(status_code=404, detail="Student not found")

    update_student(id, student.dict())
    return {"message": "Student updated successfully"}


@router.delete("/students/{id}")
def remove_student(id: int):
    if not get_student_by_id(id):
        raise HTTPException(status_code=404, detail="Student not found")

    delete_student(id)
    return {"message": "Student deleted successfully"}
