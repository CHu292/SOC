from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from sqlalchemy.orm import scoped_session, sessionmaker
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Product, Order, Log  # Import các model từ models.py
from config import DATABASE_URI, SECRET_KEY

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SECRET_KEY'] = SECRET_KEY

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Khởi tạo database
with app.app_context():
    db.create_all()

# Load user cho Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # 'user_id' ở đây sẽ khớp với 'employee_id' trong model User

# Route cho trang chào đón (URL gốc)
@app.route('/')
def index():
    return render_template('index.html')

# Route cho trang đăng nhập
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']  # Thay 'username' thành 'email'

        # Tìm người dùng dựa trên email
        user = User.query.filter_by(email=email).first()
        
        if user:
            # Nếu không có mật khẩu để kiểm tra, bạn có thể tự động đăng nhập
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            return "Email không tồn tại. Vui lòng kiểm tra lại.", 401

    return render_template('login.html')


# Route cho trang đăng ký
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        position = request.form['position']
        phone_number = request.form['phone_number']
        email = request.form['email']

        # Kiểm tra xem email có tồn tại không
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return "Email đã tồn tại. Vui lòng chọn email khác.", 400

        new_user = User(name=name, position=position, phone_number=phone_number, email=email)
        db.session.add(new_user)
        db.session.commit()
        # Đăng ký thành công, chuyển hướng về trang chủ hoặc trang đăng nhập
        return redirect(url_for('login'))
    return render_template('register.html')


# Dashboard
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', role=current_user.role)

# Route cho bảng Products (chỉ Warehouse và Admin mới có quyền)
@app.route('/view_products')
@login_required
def view_products():
    if current_user.role in ['warehouse', 'admin']:
        products = Product.query.all()
        return render_template('view_products.html', products=products)
    return "Bạn không có quyền truy cập vào bảng này.", 403

# Route cho bảng Orders (chỉ Sales và Admin mới có quyền)
@app.route('/view_orders')
@login_required
def view_orders():
    if current_user.role in ['sales', 'admin']:
        orders = Order.query.all()
        return render_template('view_orders.html', orders=orders)
    return "Bạn không có quyền truy cập vào bảng này.", 403

# Route cho bảng Logs (chỉ Admin mới có quyền)
@app.route('/view_logs')
@login_required
def view_logs():
    if current_user.role == 'admin':
        logs = Log.query.all()
        return render_template('view_logs.html', logs=logs)
    return "Bạn không có quyền truy cập vào bảng này.", 403

# Đăng xuất
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
