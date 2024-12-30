import pytest
from unittest.mock import MagicMock
from service.employee_services import remove_employee,get_employees
from model.Employee import Employee
from db.connection import engine  # Assuming 'engine' is already set up in your project

# Mocking the Session and SQLModel
# @pytest.fixture
# def mock_session(mocker):
#     # Create a mock session to simulate database interactions
#     mock_session = mocker.patch('sqlmodel.Session', autospec=True)
#     return mock_session
#
# def test_remove_employee_found(mock_session):
#     # Prepare the mock data
#     employee_id = 1
#     mock_employee = Employee(id=employee_id, name="John Doe", salary=50000, department="HR")
#
#     # Mock the behavior of `session.exec` and `session.delete`
#     mock_session.return_value.__enter__.return_value.exec.return_value.first.return_value = mock_employee
#     mock_session.return_value.__enter__.return_value.delete = MagicMock()
#     mock_session.return_value.__enter__.return_value.commit = MagicMock()
#
#     # Call the function
#     result = remove_employee(employee_id)
#
#     # Assert that the employee was deleted
#     mock_session.return_value.__enter__.return_value.delete.assert_called_once_with(mock_employee)
#     mock_session.return_value.__enter__.return_value.commit.assert_called_once()
#
#     # Assert the result is the employee that was deleted
#     assert result == mock_employee
#
# def test_remove_employee_not_found(mock_session):
#     # Prepare the mock data
#     employee_id = 999  # Assuming no employee with this ID exists
#
#     # Mock the behavior of `session.exec` to return None (i.e., employee not found)
#     mock_session.return_value.__enter__.return_value.exec.return_value.first.return_value = None
#
#     # Call the function
#     result = remove_employee(employee_id)
#
#     # Assert that no employee was deleted
#     mock_session.return_value.__enter__.return_value.delete.assert_not_called()
#     mock_session.return_value.__enter__.return_value.commit.assert_not_called()

    # Assert the result is None because the employee was not found
    # assert result is None
def test_remove_employee_invalid_type():
    """Test that the function raises an error when given a non-integer employee ID."""
    with pytest.raises(TypeError, match="Employee ID must be an integer."):
        remove_employee("invalid_id")  # Passing a string instead of an integer

def test_get_employees_no_mock_db():
    """Test that the function correctly works with an actual database (assuming it's set up in the test environment)."""
    employees = get_employees()

    # If you're running against an actual test database, you would check that the returned employees match your expectations.
    # Example:
    assert isinstance(employees, list)
    for employee in employees:
        validate_employee(employee)


def validate_employee(employee):
    """Helper method to validate the attributes of an employee object."""



    # Check that the employee is an instance of the Employee class
    assert isinstance(employee, Employee), f"Expected Employee instance, got {type(employee)}."

    # Verify that each employee has an 'id' attribute and it is a valid integer
    assert hasattr(employee, 'id'), f"Employee is missing 'id' attribute."
    assert isinstance(employee.id, int), f"Expected 'id' to be an integer, got {type(employee.id)}."
    assert  isinstance(employee.name,str)
    assert  isinstance(employee.salary,float)
    assert  isinstance(employee.department,str)

    # Optionally, check if the id is greater than 0 (assuming IDs are positive)
    assert employee.id >0, f"Expected positive 'id', got {employee.id}."
