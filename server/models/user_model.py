from sqlmodel import Field, SQLModel

class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(max_length=100)
    has_tr: bool = Field(default=False)
    tr_value: float = Field(default=0)
    tr_employee_share: float = Field(default=0)
    tr_employer_share: float = Field(default=0)
