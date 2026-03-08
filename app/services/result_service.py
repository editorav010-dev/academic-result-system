from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.marks import Mark


async def calculate_student_result(student_id: int, exam_id: int, db: AsyncSession):
    
    query = select(Mark).where(
        Mark.student_id == student_id,
        Mark.exam_id == exam_id
    )

    result = await db.execute(query)
    marks_list = result.scalars().all()

    if not marks_list:
        return None

    total_marks = sum(mark.marks_obtained for mark in marks_list)
    max_marks = sum(mark.max_marks for mark in marks_list)

    percentage = (total_marks / max_marks) * 100

    result_status = "Pass" if percentage >= 40 else "Fail"

    return {
        "student_id": student_id,
        "exam_id": exam_id,
        "total_marks": total_marks,
        "max_marks": max_marks,
        "percentage": round(percentage, 2),
        "result": result_status
    }
