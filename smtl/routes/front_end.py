from flask import Blueprint, render_template
from smtl.signup_form import SignupForm
from smtl.app import cache


blue_print = Blueprint('front_end', __name__)
cache_time = 60*60*3


@blue_print.route('/signup')
def signup():
    return render_template(
        'signup_form.html',
        title='Anmeldeformular',
        form=SignupForm()
    )


@blue_print.route('/')
@blue_print.route('/player_table')
@cache.cached(timeout=cache_time)
def player_table():
    return render_template(
        'player_table.html',
        title='Teilnehmerliste',
    )
