from database.schema import UserBase, UserDisplay
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.config import get_db
from database.user_db import create_user


router = APIRouter(
  prefix='/user',
  tags=['user']
)

@router.post('/', response_model=UserDisplay)
def create_user_endpoint(request: UserBase, db: Session = Depends(get_db)):
    db_user = create_user(db, request)
    if not db_user:
        raise HTTPException(status_code=400, detail="User could not be created")
    return db_user