import asyncio
from app.database import engine, Base, AsyncSessionLocal
from app.models import Class, User
from sqlalchemy.future import select

async def seed():
    async with AsyncSessionLocal() as db:
        # Create a test user if it doesn't exist
        result = await db.execute(select(User).filter(User.email == "test@owner.com"))
        user = result.scalars().first()
        
        if not user:
            from app.core.security import hash_password
            user = User(
                email="test@owner.com",
                hashed_password=hash_password("password123"),
                role="admin",
                is_active=True
            )
            db.add(user)
            await db.commit()
            await db.refresh(user)
            print("User created.")
        else:
            print("User exists.")

        # Create Class if it doesn't exist
        result = await db.execute(select(Class).filter(Class.name == "10th Grade"))
        class_obj = result.scalars().first()
        
        if not class_obj:
            class_obj = Class(
                name="10th Grade",
                owner_id=user.id
            )
            db.add(class_obj)
            await db.commit()
            await db.refresh(class_obj)
            print(f"Class created with ID: {class_obj.id}")
        else:
            print(f"Class exists with ID: {class_obj.id}")

if __name__ == "__main__":
    asyncio.run(seed())
