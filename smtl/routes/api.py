from flask import Blueprint, request, jsonify, render_template
from sqlalchemy.exc import SQLAlchemyError
from smtl.signup_form import SignupForm
from smtl.app import db, cache
from smtl.models.player import Player, Gender
from smtl.logging import logger
from smtl.email import default_mail


blue_print = Blueprint('api', __name__)


@blue_print.route('/add_player', methods=['POST'])
def add_player():
    form = SignupForm(request.form)
    if not form.validate():
        return jsonify(
            status='error',
            message='Formulardaten falsch oder fehlend.',
            form_errors=form.errors
        )
    try:
        p = save_player(form)
        msg = request.remote_addr + ' added ' + str(p)
        logger.info(msg)
        send_signup_mail(p, msg)
        return jsonify(status='success', message=f'{p.name} wurde hinzugefügt.')
    except SQLAlchemyError as e:
        logger.error('Database Error: ' + str(e))
        return jsonify(status='error', message='Database Error!'), 500


def send_signup_mail(p, msg):
    if default_mail:
        default_mail.send(subject=msg, body=msg + '\n\n' + render_template('auto_reply.html', player=p))


def save_player(form):
    p = Player(
        name=form.data['name'],
        gender=Gender[form.data['gender']],
        birth_year=form.data['birth_year'],
        club=form.data['club'],
        email=form.data['email'],
        dwz=form.data['dwz']
    )
    db.session.add(p)
    db.session.commit()
    return p


@blue_print.route('/get_players')
@cache.cached(timeout=60*10)
def get_players():
    players = Player.query.filter_by(approved=True).order_by(Player.dwz.desc()).all()
    return jsonify([p.to_dict() for p in players])
