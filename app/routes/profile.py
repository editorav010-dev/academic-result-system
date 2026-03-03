from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database import get_db
from app.core.dependencies import get_current_user
from app.models.school_profile import SchoolProfile
from app.models.coaching_profile import CoachingProfile
from app.schemas.profile import (
    SchoolProfileCreate,
    CoachingProfileCreate,
    ModeStatusResponse,
)
from app.models.user import User

router = APIRouter()


@router.post("/school")
async def create_school_profile(
    data: SchoolProfileCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = await db.execute(
        select(SchoolProfile).where(SchoolProfile.user_id == current_user.id)
    )
    existing = result.scalar_one_or_none()

    if existing:
        raise HTTPException(status_code=400, detail="School profile already exists")

    profile = SchoolProfile(
        user_id=current_user.id,
        school_name=data.school_name,
        school_id_code=data.school_id_code,
    )

    db.add(profile)
    await db.commit()
    await db.refresh(profile)

    return {"message": "School profile created successfully"}


@router.post("/coaching")
async def create_coaching_profile(
    data: CoachingProfileCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = await db.execute(
        select(CoachingProfile).where(CoachingProfile.user_id == current_user.id)
    )
    existing = result.scalar_one_or_none()

    if existing:
        raise HTTPException(status_code=400, detail="Coaching profile already exists")

    profile = CoachingProfile(
        user_id=current_user.id,
        institute_name=data.institute_name,
    )

    db.add(profile)
    await db.commit()
    await db.refresh(profile)

    return {"message": "Coaching profile created successfully"}


@router.get("/modes", response_model=ModeStatusResponse)
async def get_modes(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    school_result = await db.execute(
        select(SchoolProfile).where(SchoolProfile.user_id == current_user.id)
    )
    coaching_result = await db.execute(
        select(CoachingProfile).where(CoachingProfile.user_id == current_user.id)
    )

    return ModeStatusResponse(
        has_school_mode=school_result.scalar_one_or_none() is not None,
        has_coaching_mode=coaching_result.scalar_one_or_none() is not None,
    )