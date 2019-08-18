from os import environ


app_config = {
    'SECRET_KEY': environ['SECRET_KEY'], 
    'SQLALCHEMY_DATABASE_URI': environ['SQLALCHEMY_DATABASE_URI']
}


if 'EMAIL_HOST' in environ:
    email_config = {
        'HOST': environ.get('EMAIL_HOST'),
        'PORT': int(environ.get('EMAIL_PORT', 587)),
        'ADDR': environ.get('EMAIL_ADDR'),
        'USER': environ.get('EMAIL_USER'),
        'PASSWORD': environ.get('EMAIL_PASSWORD')
    }
else:
    email_config = {}


run_config = {
    'DEBUG': environ.get('DEBUG', False),
    'HOST': environ.get('HOST', '0.0.0.0'),
    'POST': int(environ.get('POST', 5000))
}
