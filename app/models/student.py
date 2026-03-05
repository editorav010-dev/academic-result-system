from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    roll_number = Column(String)

    class_id = Column(Integer, ForeignKey("classes.id"))

    student_class = relationship("Class", back_populates="students")
    marks = relationship("Mark", back_populates="student")
