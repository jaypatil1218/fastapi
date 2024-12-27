
from sqlmodel import SQLModel, Field, Session, select

class Employee(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    salary: float
    department: str

