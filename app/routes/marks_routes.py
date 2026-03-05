from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database import get_db
from app.models.marks import Mark
from app.schemas.marks import MarkCreate

router = APIRouter(prefix="/marks", tags=["Marks"])


@router.post("/")
async def create_mark(mark: MarkCreate, db: AsyncSession = Depends(get_db)):
    new_mark = Mark(**mark.dict())

    db.add(new_mark)
    await db.commit()
    await db.refresh(new_mark)

    return new_mark


@router.get("/")
async def list_marks(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Mark))
    return result.scalars().all()
