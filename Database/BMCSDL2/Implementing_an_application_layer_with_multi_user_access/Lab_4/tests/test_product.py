import pytest
from app import app
from models import db, Product

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

def test_get_products(client):
    response = client.get('/products/')
    assert response.status_code == 200

def test_add_product(client):
    response = client.post('/products/', json={'name': 'Coffee', 'price': 10.5, 'warehouse_id': None})
    assert response.status_code == 201
    assert response.json['message'] == 'Product added successfully'
