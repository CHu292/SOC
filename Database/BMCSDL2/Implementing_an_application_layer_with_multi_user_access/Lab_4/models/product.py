from models import db

class Product(db.Model):
    __tablename__ = 'product'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    
    # Khóa ngoại liên kết với Warehouse
    warehouse_id = db.Column(db.Integer, db.ForeignKey('warehouse.id'), nullable=True)
    warehouse = db.relationship('Warehouse', backref=db.backref('products', lazy=True))

    def __repr__(self):
        return f"<Product {self.name}>"
