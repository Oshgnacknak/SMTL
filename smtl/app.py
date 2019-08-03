from flask import Flask
from flask_caching import Cache
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from config import app_config, run_config

cache = Cache(config={'CACHE_TYPE': 'null' if run_config.get('DEBUG', False) else 'simple'})
csrf = CSRFProtect()
app = Flask(__name__)

app.config.from_object(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.update(app_config)

csrf.init_app(app)
cache.init_app(app)
db = SQLAlchemy(app)
