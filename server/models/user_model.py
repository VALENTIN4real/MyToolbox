from typing import Annotated, Sequence

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy import Sequence
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
    ) -> Sequence[User]:
    users = session.exec(select(User).offset(offset).limit(limit)).all()
    return users