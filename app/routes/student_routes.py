from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.database import get_db
from app.models.student import Student
from app.schemas.student import StudentCreate, StudentResponse

router = APIRouter()


@router.post("/", response_model=StudentResponse)
async def create_student(student: StudentCreate, db: AsyncSession = Depends(get_db)):
    new_student = Student(**student.dict())

    db.add(new_student)
    await db.commit()
    await db.refresh(new_student)

    return new_student


@router.get("/")
async def get_students(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Student))
    students = result.scalars().all()

    return students
