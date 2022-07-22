from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base, engine


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    employees_roles = relationship("EmployeeRole", back_populates="employee")


class CustomerRole(Base):
    __tablename__ = "customer_roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    roles = relationship("Role", back_populates="customer_role")


class BcRole(Base):
    __tablename__ = "bc_roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    roles = relationship("Role", back_populates="bc_role")


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    customer_role_id = Column(Integer, ForeignKey("customer_roles.id"))
    bc_role_id = Column(Integer, ForeignKey("bc_roles.id"))

    customer_role = relationship("CustomerRole", back_populates="roles")
    bc_role = relationship("BcRole", back_populates="roles")

    employees_roles = relationship("EmployeeRole", back_populates="role")


class EmployeeRole(Base):
    __tablename__ = 'employees_roles'

    employee_id = Column(Integer, ForeignKey('employees.id'), primary_key=True)
    role_id = Column(Integer, ForeignKey('roles.id'), primary_key=True)

    employee = relationship("Employee", back_populates="employees_roles")
    role = relationship("Role", back_populates="employees_roles")


def drop_all():
    Base.metadata.drop_all(bind=engine)


def create_all():
    Base.metadata.create_all(bind=engine)
