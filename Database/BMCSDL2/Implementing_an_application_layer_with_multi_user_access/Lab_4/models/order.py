from models import db

class Order(db.Model):
    __tablename__ = 'order'
    
    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.Date, nullable=False)
    total_amount = db.Column(db.Numeric(10, 2), nullable=False)
    
    # Khóa ngoại liên kết với Customer
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

    # Quan hệ với bảng Product thông qua bảng trung gian order_product
    products = db.relationship('Product', secondary='order_product', backref='orders', lazy=True)

    def __repr__(self):
        return f"<Order {self.id} - {self.order_date}>"
