import pytest
from app import app
from models import db, Employee

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_get_employees(client):
    response = client.get('/employees/')
    assert response.status_code == 200

def test_add_employee(client):
    response = client.post('/employees/', json={'name': 'Alice', 'position': 'Manager', 'phone_number': '987654321', 'email': 'alice@example.com'})
    assert response.status_code == 201
    assert response.json['message'] == 'Employee added successfully'
