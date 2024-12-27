from pydantic import BaseModel, ConfigDict

class EmployeeResponse(BaseModel):
    id: int
    name: str
    salary: float
    department: str

    model_config = ConfigDict(from_attributes=True)
