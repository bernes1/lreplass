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
async def read_position(position: str):
    if position == "it-utvikling":
        return "hello it-utvikling"
    elif position == "it-drift":
        return "hello it-drift"
    else: 
        return "no position spesified"

   


