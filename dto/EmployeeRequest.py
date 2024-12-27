
from pydantic import BaseModel


class EmployeeRequest(BaseModel):

    name: str
    salary: float
    department: str

    class Config:
        orm_mode = True  # Tells Pydantic to treat SQLAlchemy models as dicts
