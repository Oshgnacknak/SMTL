from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from config import app_config


csrf = CSRFProtect()
app = Flask(__name__)

app.config.from_object(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.update(app_config)

csrf.init_app(app)
db = SQLAlchemy(app)
