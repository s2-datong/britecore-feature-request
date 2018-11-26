## Requirements
- Ubuntu
- Python 2.7
- MySQL Server
- pip
- Virtualenv

## How To Setup
Run the following commands in your terminal

- git clone https://github.com/s2-datong/britecore-feature-request.git
- cd britecore-feature-request
- virtualenv venv
- source venv/bin/activate
- pip install -r requirements.txt

## Database
Create a database in mysql
mysql> CREATE DATABASE britecore;
mysql> exit;

## Config
Update the database configuration string in app/Config.py
SQLALCHEMY_DATABASE_URI = "Your connection string"

## Migration
In your terminal
- cd app
- python manage.py db init
- python manage,py db migrate
- python manage.py db upgrade

## Seeding Data
The users table created from the migrations is empty. Seed it with data in order to be able to login. The assumption is that staff should already have an account.
- mysql > use britecore;
- mysql > INSERT INTO users(firstname, lastname, username, password) VALUES('Test', 'User', 'testuser', 'password');
- mysql > exit;

## Running Test Server
cd into app directory
- python app.py
- This would start the development server 
- In your browser type http://localhost:5000