from flask import Blueprint, request, jsonify
from models import db
from models.supplier import Supplier

supplier_blueprint = Blueprint('supplier_blueprint', __name__)

@supplier_blueprint.route('/', methods=['GET'])
def get_suppliers():
    suppliers = Supplier.query.all()
    result = [{'id': s.id, 'name': s.name, 'address': s.address, 'phone_number': s.phone_number, 'email': s.email} for s in suppliers]
    return jsonify(result)

@supplier_blueprint.route('/<int:id>', methods=['GET'])
def get_supplier(id):
    supplier = Supplier.query.get_or_404(id)
    result = {'id': supplier.id, 'name': supplier.name, 'address': supplier.address, 'phone_number': supplier.phone_number, 'email': supplier.email}
    return jsonify(result)

@supplier_blueprint.route('/', methods=['POST'])
def add_supplier():
    data = request.get_json()
    new_supplier = Supplier(name=data['name'], address=data.get('address'), phone_number=data.get('phone_number'), email=data.get('email'))
    db.session.add(new_supplier)
    db.session.commit()
    return jsonify({'message': 'Supplier added successfully'}), 201
