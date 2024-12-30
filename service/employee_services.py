from http.client import HTTPException
from typing import List,Optional
from sqlmodel import Session, select
from model.Employee import Employee
from dto.EmployeeRequest import EmployeeRequest
from dto.EmployeeUpdate import EmployeeUpdate
from db.connection import engine

def create_db_and_tables():
    from sqlmodel import SQLModel
    SQLModel.metadata.create_all(engine)

def get_employees() -> List[Employee]:
    with Session(engine) as session:
        return session.exec(select(Employee)).all()

def add_employee(employee_data: EmployeeRequest) -> Employee:
    with Session(engine) as session:
        if not employee_data.name or employee_data.salary <= 0 or not employee_data.department:
            raise ValueError("Invalid employee data: Name, salary, and department must be valid.")
        new_employee = Employee(**employee_data.dict())
        session.add(new_employee)
        session.commit()
        session.refresh(new_employee)
        return new_employee


def update_employee(employee_id: int, employee_data: EmployeeUpdate) -> Optional[Employee]:
    with Session(engine) as session:
        # Log the employee ID being queried
        print(f"Looking for employee with ID: {employee_id}")

        # Execute the query
        employee = session.exec(select(Employee).where(Employee.id == employee_id)).first()

        # Log the result
        print(f"Query result: {employee}")

        if not employee:
            return None  # Employee not found

        # Update only provided fields
        for key, value in employee_data.dict(exclude_unset=True).items():
            setattr(employee, key, value)

        session.commit()
        session.refresh(employee)
        return employee





def remove_employee(employee_id: int):
    if not isinstance(employee_id, int):
        raise TypeError("Employee ID must be an integer.")

    with Session(engine) as session:
        employee = session.exec(select(Employee).where(Employee.id == employee_id))
        if employee:
            session.delete(employee)
            session.commit()

