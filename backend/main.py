from fastapi import FastAPI, Depends, HTTPException
from models import Base, JobListing
from schemas import JobSchema
from database import engine, SessionLocal
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    try:
        db = SessionLocal()
        yield db 
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/newjob")
async def add_job(request:JobSchema, db: Session = Depends(get_db)):
    job = JobListing(company_name=request.company_name, position=request.position, location=request.location, application_deadline=request.application_deadline, date_posted=request.date_posted, number_of_positions=request.number_of_positions, job_ad_link=request.job_ad_link)
    db.add(job)
    db.commit()
    db.refresh(job)
    return job


@app.get("/jobs/{position}")
async def get_jobs(position,db: Session = Depends(get_db)):
    positions = db.query(JobListing).filter(JobListing.position == position).all()
    return positions
