from pydantic import BaseModel, ConfigDict

class EmployeeRequest(BaseModel):
    name: str
    salary: float
    department: str

    model_config = ConfigDict(from_attributes=True)
