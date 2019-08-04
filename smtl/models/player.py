from smtl.app import db, current_year
from enum import Enum


class Gender(Enum):
    MALE = 'M'
    FEMALE = 'W'
    DIVERSE = 'D'


class Player(db.Model):
    id = db.Column(
        db.Integer(),
        primary_key=True,
        nullable=False
    )

    name = db.Column(
        db.String(60),
        nullable=False
    )

    gender = db.Column(
        db.Enum(Gender),
        default=Gender.DIVERSE
    )

    birth_year = db.Column(
        db.Integer(),
        nullable=False
    )

    club = db.Column(
        db.String(120)
    )

    email = db.Column(
        db.String(120),
        nullable=False
    )

    dwz = db.Column(
        db.Integer(),
        default=0
    )

    approved = db.Column(
        db.Boolean(),
        default=False
    )

    def to_dict(self):
        return {
            'name': self.name,
            'dwz': self.dwz,
            'club': self.club or '-',
            'attr': self.get_attr()
        }

    def get_attr(self):
        attr = ''
        if self.gender != Gender.MALE:
            attr += self.gender.value
        if self.birth_year >= 2001:
            attr += 'J'
        elif self.birth_year < 1960:
            attr += 'S'
        return attr

    def __str__(self):
        return f'Player({self.name})'
