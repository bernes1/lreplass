from fastapi import APIRouter, HTTPException
from models.models import JobListing
from schemas.schemas import JobSchema
from dependencies import db_dependency, user_dependency

router = APIRouter(
    prefix='/jobs',
    tags=['jobs']
)


@router.post("/newjob")
async def add_job(user: user_dependency, request:JobSchema, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")
    job = JobListing(company_name=request.company_name, position=request.position, location=request.location, application_deadline=request.application_deadline, date_posted=request.date_posted, number_of_positions=request.number_of_positions, job_ad_link=request.job_ad_link)
    db.add(job)
    db.commit()
    db.refresh(job)
    return job


@router.get("/jobs")
async def get_jobs(db: db_dependency):
    positions = db.query(JobListing).all()
    return positions

@router.get("/jobs/{position}")
async def get_jobs(position, db: db_dependency):
    positions = db.query(JobListing).filter(JobListing.position == position).all()
    return positions