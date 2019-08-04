from os import environ


meta = {
    "description": "Teilnehmerliste und Anmeldeformular der Langener Stadtmeisterschaft 2019",
    "author": "SK Langen e.V."
}

app_config = {
    'SECRET_KEY': environ['SECRET_KEY'], 
    'SQLALCHEMY_DATABASE_URI': environ['SQLALCHEMY_DATABASE_URI']
}

run_config = {
    'DEBUG': environ.get('DEBUG', False),
    'HOST': environ.get('HOST', '0.0.0.0'),
    'POST': int(environ.get('POST', 5000))
}
