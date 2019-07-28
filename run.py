from smtl.app import app, db
from smtl.routes import routes
from config import run_config
import os


def main():
	db.create_all()
	app.register_blueprint(routes)
	
	host = run_config.get('HOST', '127.0.0.1')
	port = run_config.get('PORT', 5000)
	debug = run_config.get('DEBUG', False)
	app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
	main()
