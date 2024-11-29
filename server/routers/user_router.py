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

@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, session: Session = Depends(get_session)):
    try:
        user = session.get(User, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found.")
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/users", response_model=User)
def create_user(user: User, session: Session = Depends(get_session)):
    try:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: User, session: Session = Depends(get_session)):
    try:
        db_user = session.get(User, user_id)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found.")
        for key, value in user.dict().items():
            setattr(db_user, key, value)
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/users/{user_id}")
def delete_user(user_id: int, session: Session = Depends(get_session)):
    try:
        user = session.get(User, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found.")
        session.delete(user)
        session.commit()
        return {"message": "User deleted successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))