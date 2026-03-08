from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database import get_db
from app.models.class_model import Class
from app.schemas.class_schema import ClassCreate

router = APIRouter(prefix="/classes", tags=["Classes"])

@router.post("/")
async def create_class(class_data: ClassCreate, db: AsyncSession = Depends(get_db)):
    new_class = Class(**class_data.dict())

    db.add(new_class)
    await db.commit()
    await db.refresh(new_class)

    return new_class

@router.get("/")
async def get_classes(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Class))
    classes = result.scalars().all()

    return classes
