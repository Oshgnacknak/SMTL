from smtl.app import db


class Player(db.Model):
    id = db.Column(
        db.Integer(),
        primary_key=True,
        nullable=False
    )

    firstname = db.Column(
        db.String(30),
        nullable=False
    )

    lastname = db.Column(
        db.String(30),
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

    def __repr__(self):
        return f'Player@{self.id}({self.firstname} {self.lastname})'