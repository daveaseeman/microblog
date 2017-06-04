from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # fields are instances of the db.Column class
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    # __rer__ defines how to print objects of this class (for debugging)
    def __repr__(self):
        return '<User %r>' % (self.nickname)
