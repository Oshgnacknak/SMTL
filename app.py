from flask import Flask, request, render_template, flash, redirect
from signup_form import SignupForm
from meta import meta
import os
import sys


def add_to_db(data):
	pass


# App config.
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


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



def main():
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port, debug=True)


if __name__ == '__main__':
	main()
