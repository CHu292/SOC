from app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    __table_args__ = {'schema': 'coffee_shop_schema'}
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    role = db.Column(db.String(50))

class Product(db.Model):
    __tablename__ = 'product'
    __table_args__ = {'schema': 'coffee_shop_schema'}
    
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100))
    price = db.Column(db.Integer)

class Orders(db.Model):
    __tablename__ = 'orders'
    __table_args__ = {'schema': 'coffee_shop_schema'}
    
    order_id = db.Column(db.Integer, primary_key=True)
    total_amount = db.Column(db.Integer)
    product_id = db.Column(db.Integer, db.ForeignKey('coffee_shop_schema.product.product_id'))
