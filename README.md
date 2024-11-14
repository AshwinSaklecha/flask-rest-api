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

bash
git clone https://github.com/AshwinSaklecha/flask-rest-api.git
cd flask-rest-api


2. Create and activate a virtual environment:

bash
For Unix/macOS
python -m venv venv
source venv/bin/activate
For Windows
python -m venv venv
venv\Scripts\activate



3. Install required packages:

pip install flask flask-sqlalchemy flask-migrate



## 🚦 Getting Started

1. Initialize the database:

bash
python migrations.py


2. Start the server:

bash
python run.py


The API will be available at `http://127.0.0.1:5000`

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Welcome page |
| GET | /api/v1/student | Get all students |
| POST | /api/v1/student | Create new student |
| GET | /api/v1/student/{id} | Get student by ID |
| PUT | /api/v1/student/{id} | Update student |
| DELETE | /api/v1/student/{id} | Delete student |

### API Examples

#### Create a Student

bash
curl -X POST \
http://127.0.0.1:5000/api/v1/student \
-F 'student_id=ST001' \
-F 'name=John Doe'


#### Get All Students

bash
curl http://127.0.0.1:5000/api/v1/student


#### Update a Student

bash
curl -X PUT \
http://127.0.0.1:5000/api/v1/student/1 \
-F 'student_id=ST002' \
-F 'name=Jane Doe'


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


This README.md provides:
1. Clear installation instructions
2. Detailed API documentation
3. Project structure explanation etc etc 
