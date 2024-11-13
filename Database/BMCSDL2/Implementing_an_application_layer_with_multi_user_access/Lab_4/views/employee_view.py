from flask import Blueprint, request, jsonify
from models import db
from models.employee import Employee

employee_blueprint = Blueprint('employee_blueprint', __name__)

@employee_blueprint.route('/', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    result = [{'id': e.id, 'name': e.name, 'position': e.position, 'phone_number': e.phone_number, 'email': e.email} for e in employees]
    return jsonify(result)

@employee_blueprint.route('/<int:id>', methods=['GET'])
def get_employee(id):
    employee = Employee.query.get_or_404(id)
    result = {'id': employee.id, 'name': employee.name, 'position': employee.position, 'phone_number': employee.phone_number, 'email': employee.email}
    return jsonify(result)

@employee_blueprint.route('/', methods=['POST'])
def add_employee():
    data = request.get_json()
    new_employee = Employee(name=data['name'], position=data['position'], phone_number=data.get('phone_number'), email=data.get('email'))
    db.session.add(new_employee)
    db.session.commit()
    return jsonify({'message': 'Employee added successfully'}), 201
