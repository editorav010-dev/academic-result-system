from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    class_id = Column(Integer, ForeignKey("classes.id"))

    class_obj = relationship("Class", back_populates="subjects")
    exams = relationship("Exam", back_populates="subject")
