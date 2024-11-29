from datetime import datetime
from sqlmodel import SQLModel, Field

class Operation(SQLModel, table=True):
    id: int = Field(primary_key=True)
    date: datetime = Field(default=datetime.now())
    order_amount: float = Field(default=0)