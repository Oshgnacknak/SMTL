from wtforms import Form, TextField, IntegerField, SelectField
from wtforms.validators import DataRequired, Regexp, Email, Length, NumberRange
from smtl.models.player import Gender, Player
from smtl.app import current_year


class SignupForm(Form):
	name = TextField(
		label='Name:',
		validators=[
			DataRequired('Der Name darf nicht leer sein.'),
			Length(max=Player.name.type.length, message='Der Vorname ist zu lang.')
		]
	)

	gender = SelectField(
		label='Geschlecht:',
		default=Gender.MALE.name,
		choices=[(g.name, g.value) for g in Gender]
	)

	birth_year = IntegerField(
		label='Geburtsjahr:',
		validators=[
			DataRequired('Das Geburtsjahr darf nicht leer sein.'),
			NumberRange(max=current_year, message='In der Zukumpft geboren ergibt keinen Sinn.')
		]
	)

	club = TextField(
		label='Verein:',
		validators=[
			Length(max=Player.club.type.length, message='Der Vereinsname ist zu lang.')
		]
	)

	email = TextField(
		label='EMail:',
		validators=[
			DataRequired('Die EMail darf nicht leer sein.'),
			Email('Die Email enstpricht nicht dem gewünschten Format.'),
			Length(max=Player.email.type.length, message='Die Email ist zu lang.')
		]
	)

	dwz = IntegerField(
		label='DWZ:',
		default=0,
		validators=[
			NumberRange(min=0, message='Die DWZ muss positiv sein.')
		]
	)
