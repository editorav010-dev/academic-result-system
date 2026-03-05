import asyncio
from app.database import AsyncSessionLocal
from app.models import Student, Exam
from sqlalchemy import select

async def check():
    async with AsyncSessionLocal() as db:
        students = await db.execute(select(Student))
        exams = await db.execute(select(Exam))
        print(f"Students found: {len(students.scalars().all())}")
        print(f"Exams found: {len(exams.scalars().all())}")

if __name__ == "__main__":
    asyncio.run(check())
