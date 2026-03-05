from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_db
from app.models.exam_model import Exam
from app.schemas.exam import ExamCreate

router = APIRouter(prefix="/exams", tags=["Exams"])

@router.post("/")
async def create_exam(data: ExamCreate, db: AsyncSession = Depends(get_db)):
    exam = Exam(name=data.name, subject_id=data.subject_id)
    db.add(exam)
    await db.commit()
    await db.refresh(exam)
    return exam

@router.get("/")
async def list_exams(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Exam))
    return result.scalars().all()
