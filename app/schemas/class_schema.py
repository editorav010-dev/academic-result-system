from pydantic import BaseModel

class ClassCreate(BaseModel):
    name: str

class ClassResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
