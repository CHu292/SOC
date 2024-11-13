from models import db

class Warehouse(db.Model):
    __tablename__ = 'warehouse'
    
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(50), nullable=True)
    
    # Khóa ngoại liên kết với Employee (nhân viên phụ trách)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=True)
    employee = db.relationship('Employee', backref=db.backref('warehouses', lazy=True))

    def __repr__(self):
        return f"<Warehouse {self.address} - {self.status}>"
