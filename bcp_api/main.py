from typing import List

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session
import models
import schemas
from database import SessionLocal

from services import synchronize_roles

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow everything
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/employees", response_model=List[schemas.Employee])
def employees(db: Session = Depends(get_db)):
    return db.query(models.Employee).all()


@app.get("/roles", response_model=List[schemas.Role])
def roles(db: Session = Depends(get_db)):
    return db.query(models.Role).all()


@app.get("/customer_roles", response_model=List[schemas.CustomerRole])
def customer_roles(db: Session = Depends(get_db)):
    return db.query(models.CustomerRole).all()


@app.get("/bc_roles", response_model=List[schemas.BcRole])
def bc_roles(db: Session = Depends(get_db)):
    return db.query(models.BcRole).all()


@app.get("/employees_roles", response_model=List[schemas.EmployeeRole])
def employees_roles(db: Session = Depends(get_db)):
    return db.query(models.EmployeeRole).all()


@app.post("/roles/synchronize", response_model=schemas.RolesSynchronize)
def roles_synchronize(params: schemas.RolesSynchronizeParams, db: Session = Depends(get_db)):
    """
    Synchronize roles.

    input:
    - db: database
    - params: parameters, containing
        - params.employee_id
        - params.new_customer_roles

    output:
        - dictionary of the kind
            {
                "deletedRoles": list,
                "addedRoles": list,
                "unchangedRoles": list,
                "ignoredRoles": list
            }
    """

    results = synchronize_roles(params, db)

    return results
