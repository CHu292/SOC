from flask import Flask
from flask_migrate import Migrate
from models import db
from views.customer_view import customer_blueprint
from views.order_view import order_blueprint
from views.product_view import product_blueprint
from views.employee_view import employee_blueprint
from views.warehouse_view import warehouse_blueprint
from views.supplier_view import supplier_blueprint
import config

app = Flask(__name__)
app.config.from_object(config.Config)

# Khởi tạo database với SQLAlchemy
db.init_app(app)

# Khởi tạo Flask-Migrate
migrate = Migrate(app, db)

# Đăng ký các blueprint
app.register_blueprint(customer_blueprint, url_prefix='/customers')
app.register_blueprint(order_blueprint, url_prefix='/orders')
app.register_blueprint(product_blueprint, url_prefix='/products')
app.register_blueprint(employee_blueprint, url_prefix='/employees')
app.register_blueprint(warehouse_blueprint, url_prefix='/warehouses')
app.register_blueprint(supplier_blueprint, url_prefix='/suppliers')

@app.route('/')
def home():
    return "Welcome to the Coffee Shop Management API"

if __name__ == '__main__':
    app.run(debug=True)
