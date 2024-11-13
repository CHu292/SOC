import pytest
from app import app
from models import db, Customer, Order

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

def test_get_orders(client):
    response = client.get('/orders/')
    assert response.status_code == 200

def test_add_order(client):
    customer = Customer(name='John Doe', phone_number='123456789', email='john@example.com')
    db.session.add(customer)
    db.session.commit()

    response = client.post('/orders/', json={'order_date': '2023-01-01', 'total_amount': 100.0, 'customer_id': customer.id})
    assert response.status_code == 201
    assert response.json['message'] == 'Order added successfully'
