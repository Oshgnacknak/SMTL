from os import environ


app_config = {
    'SECRET_KEY': environ['SECRET_KEY'],
    'SQLALCHEMY_DATABASE_URI': environ['SQLALCHEMY_DATABASE_URI']
}

run_config = {
    'DEBUG': environ.get('DEBUG', False),
    'HOST': environ.get('HOST', '0.0.0.0'),
    'POST': int(environ.get('POST', 5000))
}
