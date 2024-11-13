from flask import Flask
from config import Config
from auth import auth_bp
from db_operations import db_operations_bp
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(db_operations_bp, url_prefix='/dashboard')

if __name__ == '__main__':
    app.run(debug=True)
