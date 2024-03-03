from sqlalchemy import Column, Integer, String, Date
from database import Base
from schemas import JobSchema


class JobListing(Base):
    __tablename__ = "job_listings"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String)
    position = Column(String)
    location = Column(String)
    application_deadline = Column(Date)
    date_posted = Column(Date)
    number_of_positions = Column(Integer)
    job_ad_link = Column(String)
