from os import environ


app_config = {
    'SECRET_KEY': environ['SECRET_KEY'], 
    'SQLALCHEMY_DATABASE_URI': environ['SQLALCHEMY_DATABASE_URI']
}


if environ.get('EMAIL_HOST'):
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
    'DEBUG': int(environ.get('DEBUG', 0)),
    'HOST': environ.get('HOST', '0.0.0.0'),
    'PORT': int(environ.get('PORT', 5000))
}
