from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from config import config


csrf = CSRFProtect()
app = Flask(__name__)

app.config.from_object(__name__)
app.config['SECRET_KEY'] = config['SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = config.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///database.db')

csrf.init_app(app)
db = SQLAlchemy(app)
