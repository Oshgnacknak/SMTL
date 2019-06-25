from flask import Flask, request, render_template, flash, redirect
from smtl.signup_form import SignupForm
from smtl.meta import meta
from config import config
import sys


def add_to_db(data):
	pass


# App config.
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = config['SECRET_KEY']


@app.route('/signup', methods=['POST'])
def signup():
	form = SignupForm(request.form)

	if form.validate():
		add_to_db(form.data)
		flash('Spieler gespeichert!')
	else:
		for messages in form.errors.values():
			for message in messages:
				flash(message, 'error')

	return redirect('/', code=302)


@app.route('/')
@app.route('/home')
def home():
	form = SignupForm(request.form)
	return render_template(
		'home.html',
		title='Stadtmeisterschaft',
		form=form,
		meta=meta
	)
