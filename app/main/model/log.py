from .. import db


class Log(db.Model):
    """ Log Model for storing log related details """
    __tablename__ = "log"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    update_at = db.Column(db.DateTime, nullable=False)
    responsible_code = db.Column(db.Integer)
    table = db.Column(db.String(256))
    operation_code = db.Column(db.Integer)
    description = db.Column(db.String(256))

    def __repr__(self):
        return "<Log '{}'>".format(self.update_at)

