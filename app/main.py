from fastapi import FastAPI
from app.database import engine, Base
from app.routes import auth_routes, profile_routes, student_routes, subject_routes

# Import all models so Base.metadata knows about them
from app.models import user  # noqa: F401
from app.models import school_profile  # noqa: F401
from app.models import coaching_profile  # noqa: F401
from app.models import class_model  # noqa: F401
from app.models import student  # noqa: F401
from app.models import subject_model  # noqa: F401

app = FastAPI(title="EduReport")


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("startup")
async def startup():
    await create_tables()


@app.get("/")
def root():
    return {"message": "Academic Result System Running"}


# Register routers
app.include_router(auth_routes.router, prefix="/auth", tags=["Authentication"])
app.include_router(profile_routes.router, prefix="/profile", tags=["Profile"])
app.include_router(student_routes.router, prefix="/students", tags=["Students"])
app.include_router(subject_routes.router, prefix="/subjects", tags=["Subjects"])