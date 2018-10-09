from flask import Flask

# Initialize app
app = Flask(__name__, instance_relative_config=True)

# Load Views
from app import views

# Config
app.config.from_pyfile('config.py')
