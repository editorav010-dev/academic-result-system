import asyncio
from app.database import engine, Base
from app.models import user, school_profile, coaching_profile, class_model, student

async def recreate():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    print("All tables dropped and recreated successfully!")

asyncio.run(recreate())
