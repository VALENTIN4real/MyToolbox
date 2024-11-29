from typing import Annotated, List

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select

from ..database.config import SessionDep, get_session

class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(max_length=100)
    has_tr: bool = Field(default=False)
    tr_value: float = Field(default=0)
    tr_employee_share: float = Field(default=0)
    tr_employer_share: float = Field(default=0)

def get_users(
        session: Session = SessionDep,
        offset: int = 0,
        limit: Annotated[int, Query(le=100)] = 100,
    ) -> List[User]:
    users = session.exec(select(User).offset(offset).limit(limit)).all()
    return users

def get_user_by_id(session: Session, user_id: int) -> User:
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    return user

def create_user(session: Session, user: User) -> User:
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def update_user(session: Session, user_id: int, user: User) -> User:
    db_user = get_user_by_id(session, user_id)
    for key, value in user.dict().items():
        setattr(db_user, key, value)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

def delete_user(session: Session, user_id: int) -> None:
    user = get_user_by_id(session, user_id)
    session.delete(user)
    session.commit()