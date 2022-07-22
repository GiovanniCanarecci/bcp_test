# bcp

For further instructions, check the README.md files inside bcp_api and bcp_app folders

# In bcp_api

Run

    python3.10 -m venv .venv
    source .venv/bin/activate
    pipenv install -r requirements.txt
    python -m uvicorn main:app --reload

# In bcp_app
Run

    yarn install
    yarn start

# Testing application

- select one employee
- select as many or as little roles as you want (none is accepted)
- have fun testing