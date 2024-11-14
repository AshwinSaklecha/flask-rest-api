from flask import request, jsonify
from app import app
from app.module.models import Student, db
from app.module.const import HttpStatus

@app.route('/')
def index():
    return "<h1>Welcome to Flask Restful API</h1><p>Created By: Ashwin Saklecha</p>"

@app.route('/api/v1/student', methods=['GET', 'POST'])
def student():
    if request.method == 'GET':
        construct = {
            'error': [],
            'success': True,
            'student': Student.getAll()
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK
    
    elif request.method == 'POST':
        student_id = None if request.form['student_id'] is "" else request.form['student_id']
        name = None if request.form['name'] is "" else request.form['name']
        construct = {}
        try:
            mhs = Student(student_id=student_id, name=name)
            mhs.save()
            construct['success'] = True
            construct['message'] = 'Data saved'
            response = jsonify(construct)
            response.status_code = HttpStatus.CREATED
        except Exception as e:
            construct['success'] = False
            construct['error'] = str(e)
            response = jsonify(construct)
            response.status_code = HttpStatus.BAD_REQUEST
    return response
@app.route('/api/v1/student/<int:id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def studentId(id):
    mhs = Student.query.filter_by(id=id).first()
    if request.method == 'GET':
        construct = {
            'error': [],
            'success': True,
            'student': {
                'id': mhs.id,
                'student_id': mhs.student_id,
                'name': mhs.name
            }
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK
    elif request.method == 'PUT':
        student_id = None if request.form['student_id'] is "" else request.form['student_id']
        name = None if request.form['name'] is "" else request.form['name']
        construct = {}
        try:
            mhs.student_id = student_id
            mhs.name = name
            db.session.commit()
            construct['success'] = True
            construct['message'] = 'Data saved'
            response = jsonify(construct)
            response.status_code = HttpStatus.OK
        except Exception as e:
            construct['success'] = False
            construct['error'] = str(e)
            response = jsonify(construct)
            response.status_code = HttpStatus.BAD_REQUEST
    elif request.method == 'DELETE':
        construct = {}
        try:
            mhs.delete()
            construct['success'] = True
            construct['message'] = 'Data has been delete.'
            response = jsonify(construct)
            response.status_code = HttpStatus.OK
        except Exception as e:
            construct['success'] = False
            construct['error'] = str(e)
            response = jsonify(construct)
            response.status_code = HttpStatus.BAD_REQUEST
    return response