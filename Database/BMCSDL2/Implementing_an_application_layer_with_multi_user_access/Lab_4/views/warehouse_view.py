from flask import Blueprint, request, jsonify
from models import db
from models.warehouse import Warehouse

warehouse_blueprint = Blueprint('warehouse_blueprint', __name__)

@warehouse_blueprint.route('/', methods=['GET'])
def get_warehouses():
    warehouses = Warehouse.query.all()
    result = [{'id': w.id, 'address': w.address, 'status': w.status, 'employee_id': w.employee_id} for w in warehouses]
    return jsonify(result)

@warehouse_blueprint.route('/<int:id>', methods=['GET'])
def get_warehouse(id):
    warehouse = Warehouse.query.get_or_404(id)
    result = {'id': warehouse.id, 'address': warehouse.address, 'status': warehouse.status, 'employee_id': warehouse.employee_id}
    return jsonify(result)
