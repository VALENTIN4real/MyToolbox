from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlmodel import Session
from ..models.user_model import User, get_users
from ..database.config import get_session

router = APIRouter()

@router.get("/users", response_model=List[User])
def read_users(offset: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    try:
        users = get_users(session, offset, limit)
        if not users:
            raise HTTPException(status_code=404, detail="No user found.")
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))