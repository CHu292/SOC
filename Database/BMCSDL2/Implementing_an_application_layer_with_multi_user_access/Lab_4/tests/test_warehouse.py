import pytest
from app import app
from models import db, Warehouse

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

def test_get_warehouses(client):
    response = client.get('/warehouses/')
    assert response.status_code == 200

def test_add_warehouse(client):
    response = client.post('/warehouses/', json={'address': '123 Main St', 'status': 'Active', 'employee_id': None})
    assert response.status_code == 201
    assert response.json['message'] == 'Warehouse added successfully'
