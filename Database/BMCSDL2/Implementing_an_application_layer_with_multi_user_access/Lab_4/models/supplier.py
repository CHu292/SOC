from models import db

class Supplier(db.Model):
    __tablename__ = 'supplier'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=True)
    phone_number = db.Column(db.String(15), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    
    # Quan hệ với bảng Product qua bảng trung gian supplier_product
    products = db.relationship('Product', secondary='supplier_product', backref='suppliers', lazy=True)

    def __repr__(self):
        return f"<Supplier {self.name}>"
