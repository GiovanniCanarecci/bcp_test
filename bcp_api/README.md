# Installation
## Install python dependencies
Run

    python3.10 -m venv .venv
    source .venv/bin/activate
    pipenv install -r requirements.txt

## Create empty sqlite database

    source .venv/bin/activate
    python 
    >>> from models import create_all
    >>> create_all()

## Recreating sqlite database after models change

    source .venv/bin/activate
    python 
    >>> from models import drop_all, create_all
    >>> drop_all()
    >>> create_all()

## Loading database fixtures

    source .venv/bin/activate
    python 
    >>> from fixtures import install_fixtures
    >>> install_fixtures()

# Running server

    source .venv/bin/activate
    python -m uvicorn main:app --reload

# Swagger documentation

    http://127.0.0.1:8000/docs#/
