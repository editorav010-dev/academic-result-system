from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_db
from app.models.student import Student
from app.schemas.student import StudentCreate

router = APIRouter(prefix="/students", tags=["Students"])

@router.post("/")
async def create_student(student: StudentCreate, db: AsyncSession = Depends(get_db)):
    new_student = Student(**student.dict())

    db.add(new_student)
    await db.commit()
    await db.refresh(new_student)

    return new_student


@router.get("/")
async def get_students(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Student))
    return result.scalars().all()
