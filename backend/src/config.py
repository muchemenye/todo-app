import os

class Config:
    DEBUG = os.environ.get('DEBUG', 'False') == 'True'
    DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite:///todos.db')
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key_here')