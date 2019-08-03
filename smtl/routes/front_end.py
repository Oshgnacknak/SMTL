from flask import Blueprint, request, render_template, flash, redirect
from sqlalchemy.exc import SQLAlchemyError
from config import meta
from smtl.signup_form import SignupForm
from smtl.app import db, cache
from smtl.models.player import Player
from smtl.logging import logger


blue_print = Blueprint('front_end', __name__)
cache_time = 60*60*3


@blue_print.route('/signup')
def signup():
    form = SignupForm()
    return render_template(
        'signup_form.html',
        title='Anmeldeformular',
        meta=meta,
		form=form
    )


@blue_print.route('/')
@blue_print.route('/player_table')
@cache.cached(timeout=cache_time)
def player_table():
    return render_template(
        'player_table.html',
        title='Teilnehmerliste',
        meta=meta,
    )
