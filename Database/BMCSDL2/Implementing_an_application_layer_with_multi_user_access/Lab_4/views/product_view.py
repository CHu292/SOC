from flask import Blueprint, request, jsonify
from models import db
from models.product import Product

product_blueprint = Blueprint('product_blueprint', __name__)

@product_blueprint.route('/', methods=['GET'])
def get_products():
    products = Product.query.all()
    result = [{'id': p.id, 'name': p.name, 'price': str(p.price), 'warehouse_id': p.warehouse_id} for p in products]
    return jsonify(result)

@product_blueprint.route('/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    result = {'id': product.id, 'name': product.name, 'price': str(product.price), 'warehouse_id': product.warehouse_id}
    return jsonify(result)

@product_blueprint.route('/', methods=['POST'])
def add_product():
    data = request.get_json()
    new_product = Product(name=data['name'], price=data['price'], warehouse_id=data.get('warehouse_id'))
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product added successfully'}), 201

@product_blueprint.route('/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'})
