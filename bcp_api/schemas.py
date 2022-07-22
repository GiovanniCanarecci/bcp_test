from typing import List

from pydantic import BaseModel


class Employee(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class CustomerRole(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class BcRole(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class Role(BaseModel):
    id: int
    customer_role: CustomerRole
    bc_role: BcRole

    class Config:
        orm_mode = True


class EmployeeRole(BaseModel):
    employee: Employee
    role: Role

    class Config:
        orm_mode = True


class RolesSynchronizeParams(BaseModel):
    employee_id: int
    new_customer_roles: List[int]


class RolesSynchronize(BaseModel):
    deletedRoles: List[str]
    addedRoles: List[str]
    unchangedRoles: List[str]
    ignoredRoles: List[str]
