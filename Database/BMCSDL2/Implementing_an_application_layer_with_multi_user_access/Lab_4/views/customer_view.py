from flask import Blueprint, request, jsonify
from models import db
from models.customer import Customer
from utils.auth import require_role
from utils.logging import log_event

customer_blueprint = Blueprint('customer_blueprint', __name__)

# Endpoint để lấy danh sách khách hàng
@customer_blueprint.route('/', methods=['GET'])
@require_role('admin')  # Chỉ cho phép admin truy cập
def get_customers():
    log_event(action="GET_CUSTOMERS", details="Fetching all customers")  # Ghi log
    customers = Customer.query.all()
    result = [{'id': c.id, 'name': c.name, 'phone_number': c.phone_number, 'email': c.email} for c in customers]
    return jsonify(result)

# Endpoint để thêm khách hàng mới
@customer_blueprint.route('/', methods=['POST'])
@require_role('admin')  # Chỉ admin có quyền thêm khách hàng
def add_customer():
    data = request.get_json()
    new_customer = Customer(name=data['name'], phone_number=data.get('phone_number'), email=data.get('email'))
    db.session.add(new_customer)
    db.session.commit()
    log_event(action="ADD_CUSTOMER", details=f"Added customer {new_customer.name}")  # Ghi log
    return jsonify({'message': 'Customer added successfully'}), 201

# Endpoint để xóa khách hàng
@customer_blueprint.route('/<int:id>', methods=['DELETE'])
@require_role('admin')  # Chỉ admin có quyền xóa khách hàng
def delete_customer(id):
    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()
    log_event(action="DELETE_CUSTOMER", details=f"Deleted customer ID {id}")  # Ghi log
    return jsonify({'message': 'Customer deleted successfully'})
