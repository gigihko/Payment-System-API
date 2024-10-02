# FastAPI Payment System API

This is a REST API built using FastAPI for a payment system, which includes features such as registration, login, top-up, payment, transfer, transactions report, and profile update.

## Features
User Registration: Register a new user.
User Login: Authenticate an existing user and issue access tokens.
Top-up: Add funds to a user's account.

## Installation

### Requirements
- Python 3.10 or higher
- PostgreSQL

Steps
Clone the repository:
```bash
git clone https://github.com/gigihko/Payment-System-API/
cd your-project-folder
```

Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install the dependencies:
```bash
pip install -r requirements.txt
```

Set up PostgreSQL:
Ensure that PostgreSQL is installed and running on your system. You should also create a database for this project.
Example:

```bash
CREATE DATABASE payment_system;
```
Create a .env file and add the following configurations:

```bash
DATABASE_URL=postgresql://<username>:<password>@localhost:5432/<your-database-name>
SECRET_KEY=<your-secret-key>
```

## Run the Application
To start the FastAPI server:
```bash
uvicorn app.main:app --reload
```
The application will be running at http://127.0.0.1:8000.

## API Endpoints
### 1. User Registration
- URL: /register
- Method: POST
- Request Body:
```json
{
  "username": "example",
  "password": "example123",
  "email": "user@example.com"
}
```
Response:
```json
{
  "message": "User registered successfully."
}
```

### 2. User Login
- URL: /login
- Method: POST
- Request Body:
```json
{
  "username": "example",
  "password": "example123"
}
```
Response:
```json
{
  "access_token": "token",
  "token_type": "bearer"
}
```

### 3. Top Up
- URL: /topup
- Method: POST
- Request Body:
```json
{
  "amount": 100000
}
```
Response:
```json
{
  "message": "Top-up successful.",
  "balance": 100000
}
```

### Directory Structure
```bash
project-root
│
├── app/
│   ├── main.py          # The entry point of the application
│   ├── models.py        # Database models
│   ├── routes.py        # Route handlers for API endpoints
│   ├── schemas.py       # Request and response models
│   └── ...
├── alembic/
│   ├── versions/        # Database migration scripts
│   └── ...
├── .env                 # Environment variables
├── requirements.txt     # List of dependencies
└── README.md            # Project documentation
```



## Purpose

For Coding Test - Back End Developer Position



## connect with me

[Linkedin](https://www.linkedin.com/in/gigihko/)
