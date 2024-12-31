import pytest
from sqlalchemy.exc import IntegrityError
from unittest.mock import patch
from sqlmodel import Session, SQLModel
from dto.EmployeeRequest import EmployeeRequest
from model.Employee import Employee
from service.employee_services import add_employee, create_db_and_tables
from db.connection import engine
import sys

# Ensure database tables are created before running tests
@pytest.fixture(scope="module", autouse=True)
def setup_database():
    """Initialize the database schema for testing."""
    SQLModel.metadata.create_all(engine)


@pytest.fixture
def session():
    """Provide a database session for each test."""
    with Session(engine) as test_session:
        yield test_session


@pytest.fixture
def valid_employee_data():
    """Valid employee data."""
    return EmployeeRequest(name="John Doe", salary=50000.0, department="Engineering")


@pytest.fixture
def invalid_employee_data():
    """Invalid employee data."""
    return EmployeeRequest(name="", salary=-5000.0, department="")  # Invalid data


def test_add_employee_success(session, valid_employee_data):
    """Test adding a valid employee."""
    # Add the employee
    new_employee = add_employee(valid_employee_data)

    # Persist to the database
    session.add(new_employee)
    session.commit()
    session.refresh(new_employee)

    # Verify the returned employee object
    assert isinstance(new_employee, Employee)
    assert new_employee.name == "John Doe"
    assert new_employee.salary == 50000.0
    assert new_employee.department == "Engineering"

    # Verify it is persisted in the database
    db_employee = session.get(Employee, new_employee.id)
    assert db_employee is not None
    assert db_employee.name == "John Doe"
    assert db_employee.salary == 50000.0
    assert db_employee.department == "Engineering"


def test_add_employee_invalid_data(session, invalid_employee_data):
    """Test adding an employee with invalid data."""
    with pytest.raises(ValueError):  # Adjust to the specific exception raised
        add_employee(invalid_employee_data)


def test_add_employee_duplicate_name(session, valid_employee_data):
    """Test adding an employee with a duplicate name."""
    # Add the first employee
    add_employee(valid_employee_data)

    # Attempt to add another employee with the same name
    with pytest.raises(IntegrityError):  # Assuming the name field has a unique constraint
        add_employee(valid_employee_data)
