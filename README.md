# Link shortener

## Description
This project makes your links shorter.<br>
It provides web application access and API. 

## Run service:
To run the service, use the commands:
```
# Clone the repository and change directory:
git clone <github_link>
cd yacut

# Create virtual environment:
python3 -m venv venv

# Activate virtual environment:
source venv/bin/activate  # for Linux/MacOS
source venv/scripts/activate  # for windows

# Install dependencies form the "requirements.txt" file:
python3 -m pip install --upgrade pip
pip install -r requirements.txt

# Create repository for a database:
flask db init

# Create migrations:
flask db migrate -m "comment"

# Apply the migrations:
flask db upgrade 
```

## Technologies
Python 3 <br>
Flask <br>
SQLAlchemy <br>

## The author of the project
Anton Akulov - https://github.com/Nekustetnaz
