from smtl.app import app
from config import config
import os


def main():
	host = config.get('HOST', '127.0.0.1')
	port = config.get('PORT', 5000)
	debug = config.get('DEBUG', False)
	app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
	main()
