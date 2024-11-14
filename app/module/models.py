from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Student(db.Model):
    __tablename__ = 'student' #Must be defined the table name

    id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    student_id = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def __repr__(self):
        return "<Name: {}, student_id: {}>".format(self.name, self.student_id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def getAll():
        students = Student.query.all()
        result = []
        for student in students:
            obj = {
                'id': student.id,
                'student_id': student.student_id,
                'name': student.name
            }
            result.append(obj)
        return result

    def delete(self):
        db.session.delete(self)
        db.session.commit()