from pydantic import BaseModel
from typing import Optional


class SchoolProfileCreate(BaseModel):
    school_name: str
    school_id_code: Optional[str] = None


class CoachingProfileCreate(BaseModel):
    institute_name: Optional[str] = None


class ModeStatusResponse(BaseModel):
    has_school_mode: bool
    has_coaching_mode: bool
