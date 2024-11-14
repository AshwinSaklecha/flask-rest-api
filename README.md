# Student Management REST API with Flask

A simple REST API built with Flask for managing student records. This API provides basic CRUD operations for student data management with SQLite database integration.

## 🚀 Features

- RESTful API endpoints for student management
- SQLite database integration
- Error handling with proper HTTP status codes
- Student ID and Name management
- Clean project structure
- Database migrations support

## 📋 Prerequisites

- Python 3.x
- pip (Python package manager)

## 🛠️ Installation

1. Clone this repository:
   
   `git clone https://github.com/AshwinSaklecha/flask-rest-api.git`
   
   `cd flask-rest-api`

2. Create and activate a virtual environment:
   
   For Unix/macOS:
   `python -m venv venv`
   
   `source venv/bin/activate`
   
   For Windows:
   `python -m venv venv`
   
   `venv\Scripts\activate`

3. Install required packages:
   
   `pip install flask flask-sqlalchemy flask-migrate`

## 🚦 Getting Started

1. Initialize the database:
   
   `python migrations.py`

2. Start the server:
   
   `python run.py`

The API will be available at `http://127.0.0.1:5000`

## 🔌 API Endpoints

| Method | Endpoint              | Description          |
|--------|-----------------------|----------------------|
| GET    | /                     | Welcome page         |
| GET    | /api/v1/student        | Get all students     |
| POST   | /api/v1/student        | Create new student   |
| GET    | /api/v1/student/{id}   | Get student by ID    |
| PUT    | /api/v1/student/{id}   | Update student       |
| DELETE | /api/v1/student/{id}   | Delete student       |

### API Examples

#### Create a Student

Run the following in your terminal:
   
`curl -X POST http://127.0.0.1:5000/api/v1/student -F 'student_id=ST001' -F 'name=John Doe'`

#### Get All Students

Run the following in your terminal:

`curl http://127.0.0.1:5000/api/v1/student`

#### Update a Student

Run the following in your terminal:

`curl -X PUT http://127.0.0.1:5000/api/v1/student/1 -F 'student_id=ST002' -F 'name=Jane Doe'`

## 📁 Project Structure

.
├── app/
│ ├── init.py # Flask app initialization
│ ├── db/
│ │ └── flask-api.db # SQLite database
│ └── module/
│ ├── init.py
│ ├── const.py # HTTP status codes
│ ├── controller.py # API routes and logic
│ └── models.py # Database models
├── migrations.py # Database initialization
├── run.py # Application entry point
└── README.md


## 💡 Notes

- Make sure to run `migrations.py` before starting the server to set up the database schema.
- Ensure that your virtual environment is activated when working with this project.
- This API is simple and can be expanded with additional features such as authentication, validation, etc.
