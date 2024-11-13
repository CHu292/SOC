from flask import Blueprint, request, jsonify
from models import db
from models.order import Order
from models.customer import Customer

order_blueprint = Blueprint('order_blueprint', __name__)

@order_blueprint.route('/', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    result = [{'id': o.id, 'order_date': o.order_date, 'total_amount': str(o.total_amount), 'customer_id': o.customer_id} for o in orders]
    return jsonify(result)

@order_blueprint.route('/<int:id>', methods=['GET'])
def get_order(id):
    order = Order.query.get_or_404(id)
    result = {'id': order.id, 'order_date': order.order_date, 'total_amount': str(order.total_amount), 'customer_id': order.customer_id}
    return jsonify(result)

@order_blueprint.route('/', methods=['POST'])
def add_order():
    data = request.get_json()
    customer = Customer.query.get_or_404(data['customer_id'])
    new_order = Order(order_date=data['order_date'], total_amount=data['total_amount'], customer=customer)
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'message': 'Order added successfully'}), 201

@order_blueprint.route('/<int:id>', methods=['DELETE'])
def delete_order(id):
    order = Order.query.get_or_404(id)
    db.session.delete(order)
    db.session.commit()
    return jsonify({'message': 'Order deleted successfully'})
