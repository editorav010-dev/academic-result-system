from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_db
from app.models.subject_model import Subject
from app.schemas.subject_schema import SubjectCreate

router = APIRouter(prefix="/subjects", tags=["Subjects"])

@router.post("/")
async def create_subject(data: SubjectCreate, db: AsyncSession = Depends(get_db)):
    subject = Subject(name=data.name, class_id=data.class_id)
    db.add(subject)
    await db.commit()
    await db.refresh(subject)
    return subject

@router.get("/")
async def list_subjects(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Subject))
    return result.scalars().all()
