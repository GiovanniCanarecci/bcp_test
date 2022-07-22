import models
from database import SessionLocal


fixtures = {
    "employees": [
        {
            "id": 1,
            "name": "Michael"
        },
        {
            "id": 2,
            "name": "Miika"
        },
        {
            "id": 3,
            "name": "Mika"
        },
        {
            "id": 4,
            "name": "Mikka"
        },
        {
            "id": 5,
            "name": "Michele"
        },
        {
            "id": 6,
            "name": "Piergiorgio Maria Michelangelo degli Aldobrandi"
        },
    ],
    "customer_roles": [
        {
            "id": 1,
            "name": "001 - Admin"
        },
        {
            "id": 2,
            "name": "002 - Clinical personnel"
        },
        {
            "id": 3,
            "name": "003 - Warehouse personnel"
        },
    ],
    "bc_roles": [
        {
            "id": 1,
            "name": "BC_ADMIN"
        },
        {
            "id": 2,
            "name": "BC_CLINICAL"
        },
        {
            "id": 3,
            "name": "BC_WAREHOUSE"
        },
    ],
    "roles": [
        {
            # "id": 1,
            "customer_role_id": 1,
            "bc_role_id": 1
        },
        {
            # "id": 2,
            "customer_role_id": 2,
            "bc_role_id": 2
        },
        {
            # "id": 3,
            "customer_role_id": 3,
            "bc_role_id": 3
        },
    ],
    "employees_roles": [
        {
            "employee_id": 1,
            "role_id": 1
        },
        {
            "employee_id": 1,
            "role_id": 2
        },
        {
            "employee_id": 2,
            "role_id": 3
        },
        {
            "employee_id": 3,
            "role_id": 1
        },
        {
            "employee_id": 4,
            "role_id": 1
        },
        {
            "employee_id": 4,
            "role_id": 3
        },
        {
            "employee_id": 5,
            "role_id": 2
        },
        {
            "employee_id": 6,
            "role_id": 1
        },
        {
            "employee_id": 6,
            "role_id": 2
        },
        {
            "employee_id": 6,
            "role_id": 3
        },
    ],
}


def install_fixture(fixture, model, db=None):
    if not db:
        db = SessionLocal()

    entity = model(**fixture)
    db.add(entity)
    db.commit()


def install_fixtures():
    db = SessionLocal()

    for name, model in zip(
        ['employees', 'customer_roles', 'bc_roles', 'roles', 'employees_roles'],
        [models.Employee, models.CustomerRole, models.BcRole, models.Role, models.EmployeeRole]
    ):
        for fixture in fixtures[name]:
            install_fixture(fixture, model, db=db)
