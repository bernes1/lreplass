from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Job(BaseModel):
    company: str
    position: str
    location: str
    applicationDeadLine: str
    datePosted: str
    numberOfPosition: int
    jobAdLink: str
    


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/{position}")
async def read_position():
    if job.position == "it-utvikloimng":
        print("hello it-utvikling")
    return "yeat"
   


