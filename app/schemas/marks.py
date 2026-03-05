from pydantic import BaseModel

class MarkCreate(BaseModel):
    student_id: int
    exam_id: int
    marks_obtained: int
    max_marks: int
