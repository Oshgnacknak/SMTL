from wtforms import Form, TextField, IntegerField
from wtforms.validators import DataRequired, Regexp, Email, Length, NumberRange
import re


class SignupForm(Form):
	firstname = TextField(
		label='Vorname:',
		validators=[
			DataRequired('Der Vorname darf nicht leer sein.'),
			Length(max=30, message='Der Vorname ist zu lang.')
		]
	)

	lastname = TextField(
		label='Nachname:',
		validators=[
			DataRequired('Der Nachname darf nicht leer sein.'),
			Length(max=30, message='Der Nachname ist zu lang.')
		]
	)

	club = TextField(
		label='Verein:',
		validators=[
			Length(max=120, message='Der Vereinsname ist zu lang.')
		]
	)

	email = TextField(
		label='EMail:',
		validators=[
			DataRequired('Die EMail darf nicht leer sein.'),
			Email('Die Email enstpricht nicht dem gewünschten Format.'),
			Length(max=120, message='Die Email ist zu lang.')
		]
	)

	dwz = IntegerField(
		label='DWZ:',
		default=0,
		validators=[
			NumberRange(min=0, message='Die DWZ ist zu klein.')
		]
	)
