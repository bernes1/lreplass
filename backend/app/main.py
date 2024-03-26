from fastapi import FastAPI, Depends, HTTPException
from models.models import Base, JobListing
from schemas.schemas import JobSchema
from database.configuration import engine, SessionLocal
from dependencies import db_dependency, user_dependency
import auth as auth
import routers.jobs as jobs

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth.router)
app.include_router(jobs.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/user")
async def user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")
    return{"User": user}

