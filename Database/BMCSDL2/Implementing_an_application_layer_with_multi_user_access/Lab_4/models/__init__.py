from flask_sqlalchemy import SQLAlchemy

# Khởi tạo SQLAlchemy
db = SQLAlchemy()

# Bảng liên kết giữa Order và Product
order_product = db.Table('order_product',
    db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True)
)

# Bảng liên kết giữa Supplier và Product
supplier_product = db.Table('supplier_product',
    db.Column('supplier_id', db.Integer, db.ForeignKey('supplier.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True)
)

# Import các mô hình khác
from models.customer import Customer
from models.order import Order
from models.product import Product
from models.employee import Employee
from models.warehouse import Warehouse
from models.supplier import Supplier
from models.log import Log
