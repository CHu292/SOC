from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import db
import os

def get_database_session():
    """
    Trả về một phiên làm việc với cơ sở dữ liệu.
    """
    # Tạo engine từ URL cơ sở dữ liệu
    DATABASE_URL = os.getenv("DATABASE_URL")
    engine = create_engine(DATABASE_URL)
    
    # Khởi tạo sessionmaker
    Session = sessionmaker(bind=engine)
    return Session()

def init_db(app):
    """
    Khởi tạo cơ sở dữ liệu trong ứng dụng Flask.
    """
    with app.app_context():
        db.create_all()
        print("Database initialized!")
