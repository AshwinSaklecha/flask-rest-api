# Flask Student Management System API

A RESTful API built with Flask for managing student records. This API provides comprehensive CRUD operations for student data management with database integration.

## 🚀 Features

- RESTful API endpoints for student management
- Database integration (SQLite in development, PostgreSQL in production)
- Error handling with proper HTTP status codes
- Student data management (ID, Name)
- Clean project structure
- Database migrations support
- Production-ready configuration

## 📋 Prerequisites

- Python 3.x
- pip (Python package manager)

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AshwinSaklecha/flask-rest-api.git
   cd flask-rest-api
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Initialize the database:
   ```bash
   python migrations.py
   ```

4. Run the application:
   ```bash
   python run.py
   ```

## 🔧 Configuration

- Development: SQLite database (automatically configured)
- Production: PostgreSQL database (configured via environment variables)

## 📚 API Endpoints

### Base URL
`http://localhost:5000/api/v1`

### Available Endpoints

#### Students
- `GET /student` - Get all students
- `POST /student` - Create a new student
- `GET /student/<id>` - Get a specific student
- `PUT /student/<id>` - Update a student
- `DELETE /student/<id>` - Delete a student

### Request/Response Examples

#### Get All Students
```json
GET /api/v1/student

Response:
{
    "error": [],
    "success": true,
    "student": [
        {
            "id": 1,
            "student_id": "12345",
            "name": "John Doe"
        }
    ]
}
```

#### Get Single Student
```json
GET /api/v1/student/1

Response:
{
    "error": [],
    "success": true,
    "student": {
        "id": 1,
        "student_id": "12345",
        "name": "John Doe"
    }
}
```

#### Create Student
```http
POST /api/v1/student
Content-Type: application/x-www-form-urlencoded

student_id=12345&name=John Doe

Response:
{
    "success": true,
    "message": "Data saved"
}
```

#### Update Student
```http
PUT /api/v1/student/1
Content-Type: application/x-www-form-urlencoded

student_id=12345&name=John Updated

Response:
{
    "success": true,
    "message": "Data saved"
}
```

#### Delete Student
```json
DELETE /api/v1/student/1

Response:
{
    "success": true,
    "message": "Data has been delete."
}
```



## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details

## 👤 Author

Created by: Ashwin Saklecha
