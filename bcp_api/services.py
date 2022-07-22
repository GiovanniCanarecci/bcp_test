import models


def synchronize_roles(params, db):

    # print("")
    # print("Paramenters")
    # print(params)
    # print("")

    all_bc_roles = db.query(models.BcRole).all()

    # ~~~~~~~~~~~~~~~~
    # Get the employee
    # ~~~~~~~~~~~~~~~~

    employee_id = params.employee_id

    # print("Employee ID")
    # print(employee_id)
    # print("")

    employee = db.query(models.Employee).filter(
        models.Employee.id == employee_id).first()

    # Test
    # employee = db.query(models.Employee).filter(models.Employee.id == 70).first()

    if not employee:
        # There is no employee with that ID
        return {
            "deletedRoles": [],
            "addedRoles": [],
            "unchangedRoles": [],
            "ignoredRoles": [r.name for r in all_bc_roles]
        }

    # print("Employee")
    # print(employee)
    # print(employee.id)
    # print(employee.name)
    # print("")

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Get the new customer roles and so the new BC roles
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    new_customer_roles_ids = params.new_customer_roles

    # print("New Customer Roles IDs")
    # print(new_customer_roles_ids)
    # print("")

    # Note that new_customer_roles can also be empty
    new_customer_roles = db.query(models.CustomerRole).filter(
        models.CustomerRole.id.in_(new_customer_roles_ids)).all()

    # print("New Customer Roles")
    # print(new_customer_roles)
    # print("")

    new_bc_roles = []

    for new_customer_role in new_customer_roles:
        # new_customer_role.role is a list because a customer_role in theory can be associated to multiple roles
        for role in new_customer_role.roles:
            new_bc_roles.append(role.bc_role)

            # print(role.bc_role)
            # print(role.bc_role.id)
            # print(role.bc_role.name)

        # print("")

    # print("New Bc Roles")
    # print(new_bc_roles)
    # print("")

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Get the old BC roles that the employee has
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    old_bc_roles = [oer.role.bc_role for oer in employee.employees_roles]

    # print("Old Bc Roles")
    # print(old_bc_roles)
    # print("")

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Compare the old and new bc roles
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    unchanged_bc_roles = list(
        set(old_bc_roles).intersection(set(new_bc_roles)))

    deleted_bc_roles = list(set(old_bc_roles) - set(new_bc_roles))

    added_bc_roles = list(set(new_bc_roles) - set(old_bc_roles))

    ignored_bc_roles = list(
        set(all_bc_roles) - set(old_bc_roles).union(set(new_bc_roles)))

    # ~~~~~~~~~~~~~~~~~
    # Return only names
    # ~~~~~~~~~~~~~~~~~

    unchanged_bc_roles_names = [r.name for r in unchanged_bc_roles]

    deleted_bc_roles_names = [r.name for r in deleted_bc_roles]

    added_bc_roles_names = [r.name for r in added_bc_roles]

    ignored_bc_roles_names = [r.name for r in ignored_bc_roles]

    # print("unchanged_bc_roles")
    # print(unchanged_bc_roles)
    # print(unchanged_bc_roles_names)
    # print("")

    # print("deleted_bc_roles")
    # print(deleted_bc_roles)
    # print(deleted_bc_roles_names)
    # print("")

    # print("added_bc_roles")
    # print(added_bc_roles)
    # print(added_bc_roles_names)
    # print("")

    # print("ignored_bc_roles")
    # print(ignored_bc_roles)
    # print(ignored_bc_roles_names)
    # print("")

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Save the changes into database
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # For each bc_role ...
    for deleted_bc_role in deleted_bc_roles:
        # In our generalization, a bc_role can be associated to many Roles
        for role in deleted_bc_role.roles:
            db.query(models.EmployeeRole).filter(
                models.EmployeeRole.role == role,
                models.EmployeeRole.employee == employee,
            ).delete()

    # For each bc_role ...
    for added_bc_role in added_bc_roles:
        # In our generalization, a bc_role can be associated to many Roles
        for role in added_bc_role.roles:
            new_employee_role = models.EmployeeRole(
                employee=employee,
                role=role
            )
            db.add(new_employee_role)

    db.commit()

    return {
        "deletedRoles": deleted_bc_roles_names,
        "addedRoles": added_bc_roles_names,
        "unchangedRoles": unchanged_bc_roles_names,
        "ignoredRoles": ignored_bc_roles_names
    }
