# «YaCut» - link shortener

### Description
The YaCut project is a link shortening service. Its purpose is to associate a long user link with a short one, which is offered by the user himself or provided by the service.<br>
It provides web application access and API. 

### API access
The API of the project is available for everyone. <br>
The service provides two endpoints:<br>
```/api/id/  # POST request to create a new short link```<br>
```/api/id/<short_id>/  # GET request to get the original link by the specified short identifier```

### Run project
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

### Technologies
Python 3 <br>
Flask <br>
SQLAlchemy <br>

### The author of the project
Anton Akulov - https://github.com/Nekustetnaz
