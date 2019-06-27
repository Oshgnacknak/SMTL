from flask import Blueprint, request, render_template, flash, redirect
from sqlalchemy.exc import SQLAlchemyError
from smtl.signup_form import SignupForm
from smtl.meta import meta
from smtl.app import db
from smtl.models.player import Player
import sys


routes = Blueprint('routes', __name__)


@routes.route('/signup', methods=['POST'])
def signup():
    form = SignupForm(request.form)
    if form.validate():
        p = Player(
            name=form.data['name'],
            club=form.data['club'],
            email=form.data['email'],
            dwz=form.data['dwz']
        )
        print(f'{request.remote_addr} is trying to add {p}', file=sys.stderr)
        try:
            db.session.add(p)
            db.session.commit()
        except SQLAlchemyError as e:
            print(e, file=sys.stderr)
            return 'Database Error!', 500
        flash(f'{p.name} wurde hinzugefügt.')
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
        meta=meta,
		players=Player.query.all()
    )
