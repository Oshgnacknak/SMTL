from flask import Blueprint, request, render_template, flash, redirect
from smtl.signup_form import SignupForm
from smtl.meta import meta


routes = Blueprint('routes', __name__)


@routes.route('/signup', methods=['POST'])
def signup():
	form = SignupForm(request.form)

	if form.validate():
		# add_to_db(form.data)
		flash('Spieler gespeichert!')
	else:
		for messages in form.errors.values():
			for message in messages:
				flash(message, 'error')

	return redirect('/', code=302)


@routes.route('/')
@routes.route('/home')
def home():
	form = SignupForm(request.form)
	return render_template(
		'home.html',
		title='Stadtmeisterschaft',
		form=form,
		meta=meta
	)
