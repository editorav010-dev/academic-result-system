from pydantic import BaseModel


class SubjectCreate(BaseModel):
    name: str
    class_id: int


class SubjectResponse(BaseModel):
    id: int
    name: str
    class_id: int

    class Config:
        from_attributes = True
