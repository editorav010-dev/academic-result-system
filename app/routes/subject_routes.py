from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database import get_db
from app.models.subject_model import Subject
from app.schemas.subject import SubjectCreate, SubjectResponse

router = APIRouter()


@router.post("/", response_model=SubjectResponse)
async def create_subject(subject: SubjectCreate, db: AsyncSession = Depends(get_db)):
    new_subject = Subject(name=subject.name, class_id=subject.class_id)

    db.add(new_subject)
    await db.commit()
    await db.refresh(new_subject)

    return new_subject


@router.get("/", response_model=list[SubjectResponse])
async def list_subjects(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Subject))
    subjects = result.scalars().all()

    return subjects
