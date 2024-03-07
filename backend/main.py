from fastapi import FastAPI, Depends, HTTPException
from models import Base, JobListing
from schemas import JobSchema
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import Annotated
import auth
from auth import get_current_user

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth.router)

def get_db():
    try:
        db = SessionLocal()
        yield db 
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/user")
async def user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")
    return{"User": user}



@app.post("/newjob")
async def add_job(user: user_dependency, request:JobSchema, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")
    job = JobListing(company_name=request.company_name, position=request.position, location=request.location, application_deadline=request.application_deadline, date_posted=request.date_posted, number_of_positions=request.number_of_positions, job_ad_link=request.job_ad_link)
    db.add(job)
    db.commit()
    db.refresh(job)
    return job


@app.get("/jobs")
async def get_jobs(db: db_dependency):
    positions = db.query(JobListing).all()
    return positions

@app.get("/jobs/{position}")
async def get_jobs(position, db: db_dependency):
    positions = db.query(JobListing).filter(JobListing.position == position).all()
    return positions
