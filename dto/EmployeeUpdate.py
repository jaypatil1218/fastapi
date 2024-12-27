from typing import Optional
from pydantic import BaseModel

class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    salary: Optional[float] = None
    department: Optional[str] = None

