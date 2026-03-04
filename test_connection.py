"""Quick test to verify database connectivity."""
import asyncio
import asyncpg
from app.config import settings

# Extract raw connection string (replace +asyncpg with empty for asyncpg lib)
DSN = settings.DATABASE_URL.replace("postgresql+asyncpg://", "postgresql://")


async def test():
    try:
        conn = await asyncpg.connect(DSN)
        version = await conn.fetchval("SELECT version();")
        print("✅ Database connection successful!")
        print(f"   PostgreSQL version: {version}")

        # Check if tables were created by FastAPI lifespan
        tables = await conn.fetch(
            "SELECT tablename FROM pg_tables WHERE schemaname = 'public';"
        )
        if tables:
            print(f"   Tables found: {', '.join(t['tablename'] for t in tables)}")
        else:
            print("   No tables yet (start uvicorn first to auto-create them).")

        await conn.close()
    except Exception as e:
        print(f"❌ Connection failed: {e}")


asyncio.run(test())
