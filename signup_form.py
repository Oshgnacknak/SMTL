from wtforms import Form, TextField, IntegerField
from wtforms.validators import DataRequired, Regexp, Email
import re


name_regex = re.compile('[A-Za-z]+')


class SignupForm(Form):
	firstname = TextField(
		label='Vorname:', 
		validators=[
			DataRequired('Der Vorname darf nicht leer sein.'),
			Regexp(name_regex, message='Der Vorname enstpricht nicht dem gewünschten Format.')
		]
	)

	lastname = TextField(
		label='Nachname:', 
		validators=[
			DataRequired('Der Nachname darf nicht leer sein.'), 
			Regexp(name_regex, message='Der Nachname enstpricht nicht dem gewünschten Format.')
		]
	)

	club = TextField(
		label='Verein:'
	)

	email = TextField(
		label='EMail:', 
		validators=[
			DataRequired('Die EMail darf nicht leer sein.'),
			Email('Die Email enstpricht nicht dem gewünschten Format.')
		]
	)

	dwz = IntegerField(
		label='DWZ:',
		default=0
	)