from pydantic import BaseModel

class ExamCreate(BaseModel):
    name: str
    subject_id: int
