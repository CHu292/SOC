import os

DATABASE_URI = os.getenv("DATABASE_URI", "postgresql+psycopg2://postgres:0209@localhost/lab3")
SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
