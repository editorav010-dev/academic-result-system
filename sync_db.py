import asyncio
from app.database import engine, Base
from app.models import user, school_profile, coaching_profile, class_model, student, subject_model

async def recreate():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("All tables synced successfully!")

asyncio.run(recreate())
