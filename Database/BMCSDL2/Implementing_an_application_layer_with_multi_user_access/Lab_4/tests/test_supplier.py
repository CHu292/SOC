import pytest
from app import app
from models import db, Supplier

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

def test_get_suppliers(client):
    response = client.get('/suppliers/')
    assert response.status_code == 200

def test_add_supplier(client):
    response = client.post('/suppliers/', json={'name': 'Global Suppliers', 'address': '456 Market St', 'phone_number': '1231231234', 'email': 'contact@globalsuppliers.com'})
    assert response.status_code == 201
    assert response.json['message'] == 'Supplier added successfully'
