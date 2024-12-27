from fastapi import FastAPI, HTTPException
import logging
from service.employee_services import get_employees,update_employee,add_employee,remove_employee,create_db_and_tables
from dto.EmployeeRequest import EmployeeRequest
from dto.EmployeeResponce import EmployeeResponse
from dto.EmployeeUpdate import EmployeeUpdate

from typing import List
logger = logging.getLogger(__name__)
app = FastAPI()
print("just testing")
# Initialize the database
@app.on_event("startup")
def startup():
    create_db_and_tables()

@app.get("/employees", response_model=List[EmployeeResponse])
def list_employees():
    print("inside get method")
    return get_employees()

@app.post("/employees", response_model=EmployeeResponse)
def create_employee(employee: EmployeeRequest):
    return add_employee(employee)


@app.put("/employees/{employee_id}", response_model=EmployeeResponse)
def modify_employee(employee_id: int, employee: EmployeeUpdate):
    updated_employee = update_employee(employee_id, employee)
    logger.info(updated_employee)
    if not updated_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated_employee


@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    if not isinstance(employee_id, int):
        raise TypeError("Employee ID must be an integer.")
    logger.info(employee_id)
    remove_employee(employee_id)
    return {"msg":"deleted"}
