from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Mark(Base):
    __tablename__ = "marks"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(Integer, ForeignKey("students.id"))
    exam_id = Column(Integer, ForeignKey("exams.id"))

    marks_obtained = Column(Integer)
    max_marks = Column(Integer)

    student = relationship("Student", back_populates="marks")
    exam = relationship("Exam", back_populates="marks")
