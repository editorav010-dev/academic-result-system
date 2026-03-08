from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database import get_db
from app.models.student import Student
from app.models.marks import Mark
from app.models.exam_model import Exam
from app.models.subject_model import Subject
from app.services.result_service import calculate_student_result

router = APIRouter(prefix="/results", tags=["Results"])

@router.get("/student/{student_id}")
async def get_student_result(student_id: int, db: AsyncSession = Depends(get_db)):
    # Check if student exists
    student_query = await db.execute(select(Student).where(Student.id == student_id))
    student = student_query.scalar_one_or_none()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Fetch marks for that student
    marks_query = await db.execute(select(Mark).where(Mark.student_id == student_id))
    marks = marks_query.scalars().all()

    if not marks:
        return {
            "student": student.name,
            "message": "No marks found"
        }

    subjects_data = []
    total_marks = 0
    max_total = 0

    for mark in marks:
        # Fetch exam first to get subject_id
        exam_query = await db.execute(select(Exam).where(Exam.id == mark.exam_id))
        exam = exam_query.scalar_one()

        subject_query = await db.execute(select(Subject).where(Subject.id == exam.subject_id))
        subject = subject_query.scalar_one()

        subjects_data.append({
            "subject": subject.name,
            "marks": mark.marks_obtained,
            "max_marks": mark.max_marks
        })

        total_marks += mark.marks_obtained
        max_total += mark.max_marks

    percentage = (total_marks / max_total) * 100 if max_total > 0 else 0

    return {
        "student": student.name,
        "subjects": subjects_data,
        "total_marks": total_marks,
        "max_marks": max_total,
        "percentage": round(percentage, 2)
    }

@router.get("/student/{student_id}/exam/{exam_id}")
async def get_student_result_by_exam(
    student_id: int,
    exam_id: int,
    db: AsyncSession = Depends(get_db)
):
    
    result = await calculate_student_result(student_id, exam_id, db)

    if not result:
        raise HTTPException(status_code=404, detail="Marks not found")

    return result
