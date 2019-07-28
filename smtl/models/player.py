from smtl.app import db


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

    def __str__(self):
        return f'Player({self.name})'
