from fastapi import Depends
from sqlalchemy.orm import Session
from database.configuration import SessionLocal
from auth import get_current_user
from typing import Annotated

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
    
db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]