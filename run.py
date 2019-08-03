from smtl.app import app, db
from smtl.routes import front_end_blue_print, api_blue_print
from config import run_config
import os


def main():
	db.create_all()

	app.register_blueprint(front_end_blue_print)
	app.register_blueprint(api_blue_print, url_prefix='/api')

	host = run_config.get('HOST', '127.0.0.1')
	port = run_config.get('PORT', 5000)
	debug = run_config.get('DEBUG', False)

	app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
	main()
