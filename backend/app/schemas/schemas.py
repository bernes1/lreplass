from datetime import date
from pydantic import BaseModel

class JobSchema(BaseModel):
    id: int
    company_name: str
    position: str
    location: str
    application_deadline: date
    date_posted: date
    number_of_positions: int
    job_ad_link: str