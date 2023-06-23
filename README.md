# Link shortener

## Description
This project makes your links shorter.<br>
It provides web application access and API. 

## Run service:
To run the service, use the commands:
```
git clone
cd yacut
python3 -m venv venv
source venv/bin/activate  # for Linux/MacOS
source venv/scripts/activate  # for windows
python3 -m pip install --upgrade pip
pip install -r requirements.txt
flask db init
flask db migrate -m "comment"
flask db upgrade 
```

## Technologies
Python 3 <br>
Flask <br>
SQLAlchemy <br>

## The author of the project
Anton Akulov - https://github.com/Nekustetnaz
