import pytest
from app import app
from models import db, Customer

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Sử dụng SQLite trong bộ nhớ cho kiểm thử
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_get_customers(client):
    response = client.get('/customers/')
    assert response.status_code == 200

def test_add_customer(client):
    response = client.post('/customers/', json={'name': 'John Doe', 'phone_number': '123456789', 'email': 'john@example.com'})
    assert response.status_code == 201
    assert response.json['message'] == 'Customer added successfully'
