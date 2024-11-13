from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ = 'employee'
    __table_args__ = {'schema': 'coffee_shop_schema'}

    employee_id = db.Column(db.Integer, primary_key=True)  # Khóa chính
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(13))
    email = db.Column(db.String(100))


class Product(db.Model):
    __tablename__ = 'product'
    __table_args__ = {'schema': 'coffee_shop_schema'}
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

class Order(db.Model):
    __tablename__ = 'orders'
    __table_args__ = {'schema': 'coffee_shop_schema'}
    
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(50), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('coffee_shop_schema.product.id'))
    employee_id = db.Column(db.Integer, db.ForeignKey('coffee_shop_schema.employee.employee_id'))  # Tham chiếu đến 'employee_id'
    quantity = db.Column(db.Integer, nullable=False)

class Log(db.Model):
    __tablename__ = 'main_log'
    __table_args__ = {'schema': 'coffee_shop_schema'}
    
    id = db.Column(db.Integer, primary_key=True)
    operation = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)  # Có thể là employee_id nếu đây là ID người dùng
    timestamp = db.Column(db.DateTime, nullable=False)
