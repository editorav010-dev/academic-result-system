from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    roll_number = Column(String, nullable=False)

    class_id = Column(Integer, ForeignKey("classes.id"), nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    student_class = relationship("Class", back_populates="students")
