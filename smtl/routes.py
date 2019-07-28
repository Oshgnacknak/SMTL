from flask import Blueprint, request, render_template, flash, redirect
from sqlalchemy.exc import SQLAlchemyError
from smtl.signup_form import SignupForm
from smtl.meta import meta
from smtl.app import db
from smtl.models.player import Player
from smtl.logging import logger


routes = Blueprint('routes', __name__)


@routes.route('/signup', methods=['POST'])
def signup():
    form = SignupForm(request.form)
    if form.validate():
        try:
            p = add_player(form)
            logger.info(request.remote_addr + ' added ' + str(p))
        except SQLAlchemyError as e:
            logger.error('Database Error: ' + e)
            return 'Database Error!', 500
    else:
        show_errors(form)
    return redirect('/', code=302)


def add_player(form):
    p = Player(
        name=form.data['name'],
        club=form.data['club'],
        email=form.data['email'],
        dwz=form.data['dwz']
    )
    db.session.add(p)
    db.session.commit()
    flash(f'{p.name} wurde hinzugefügt.')
    return p


def show_errors(form):
    for messages in form.errors.values():
        for message in messages:
            flash(message, 'error')


@routes.route('/')
@routes.route('/home')
def home():
    form = SignupForm(request.form)
    return render_template(
        'home.html',
        title='Stadtmeisterschaft',
        form=form,
        meta=meta,
		players=Player.query.filter_by(approved=True).all()
    )
