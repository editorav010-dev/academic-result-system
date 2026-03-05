from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    roll_number: str
    class_id: int

class StudentResponse(BaseModel):
    id: int
    name: str
    roll_number: str
