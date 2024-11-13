from flask import Blueprint, render_template
from flask_login import login_required
from models import Product, Orders
from app import db

db_operations_bp = Blueprint('db_operations', __name__)

@db_operations_bp.route('/dashboard')
@login_required
def dashboard():
    products = Product.query.all()
    return render_template('dashboard.html', products=products)

@db_operations_bp.route('/add_product', methods=['POST'])
@login_required
def add_product():
    new_product = Product(product_name=request.form['name'], price=request.form['price'])
    db.session.add(new_product)
    db.session.commit()
    return redirect(url_for('db_operations.dashboard'))
