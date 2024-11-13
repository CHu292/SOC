from models import db
from datetime import datetime

class Log(db.Model):
    __tablename__ = 'log'
    
    id = db.Column(db.Integer, primary_key=True)
    operation_type = db.Column(db.String(10), nullable=False)  # Thêm, Sửa, Xóa
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user_id = db.Column(db.Integer, nullable=True)  # ID của người dùng thực hiện thay đổi
    changed_data = db.Column(db.JSON, nullable=True)  # Lưu trữ dữ liệu đã thay đổi

    def __repr__(self):
        return f"<Log {self.operation_type} - {self.timestamp}>"
