from sqlmodel import SQLModel, Field, create_engine, Session, select
from dto.EmployeeResponce import EmployeeResponse
from dto.EmployeeRequest import EmployeeRequest
from typing import List
from pydantic import BaseModel

# Corrected database URL
database_url = "cockroachdb+psycopg2://jay:dhEOwFiYtRthwMBhULHDLA@slick-knight-6482.j77.aws-ap-south-1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&sslrootcert=C:/Users/wdila/appdata/roaming/postgresql/root.crt"

# Create engine
engine = create_engine(database_url)

print("just testing ")
# Define the Employee model with primary key and data types
class Employee(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    salary: float
    department: str


# Pydantic model for response

# Function to create database and tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# Function to get all employees (sync version for now)
def get_employees() -> List[Employee]:
    with Session(engine) as session:
        statement = select(Employee)
        all_employees = session.exec(statement).all()
        for employee in all_employees:
            print(employee)
        return all_employees


# Function to add a new employee (optional)
def add_employee(name: str, salary: float, department: str):
    with Session(engine) as session:
        new_employee = Employee(name=name, salary=salary, department=department)
        session.add(new_employee)
        session.commit()


def remove_employee(id: int):
    with Session(engine) as session:
        employee = session.query(Employee).filter(Employee.id == id).first()
        if employee:
            session.delete(employee)
            session.commit()
        return employee


def delete_employee_name(employee_name):
    with Session(engine) as session:
        employees = session.query(Employee).filter(Employee.name == employee_name).all()
        if employees:
            for employee in employees:
                session.delete(employee)
                session.commit()
        return employee


def update_employee(employee_id: int, employee_data: EmployeeRequest) -> EmployeeResponse:
    with Session(engine) as session:
        # Find the employee by ID
        employee_to_update = session.query(Employee).filter(Employee.id == employee_id).first()

        if not employee_to_update:
            return None  # Employee not found

        # Update employee's data
        employee_to_update.name = employee_data.name
        employee_to_update.salary = employee_data.salary
        employee_to_update.department = employee_data.department

        # Commit the changes
        session.commit()

        # Refresh the session to get the latest data
        session.refresh(employee_to_update)

        # Return the updated employee as a Pydantic model (EmployeeResponse)
        return employee_to_update


# Call the function to create tables if not already created
create_db_and_tables()
get_employees()