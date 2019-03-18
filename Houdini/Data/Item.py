from Houdini.Data import db


class Item(db.Model):
    __tablename__ = 'item'

    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(50))
    Type = db.Column(db.SmallInteger, nullable=False, server_default=db.text("1"))
    Cost = db.Column(db.Integer, nullable=False, server_default=db.text("0"))
    Member = db.Column(db.Boolean, nullable=False, server_default=db.text("false"))
    Bait = db.Column(db.Boolean, nullable=False, server_default=db.text("false"))
    Patched = db.Column(db.Boolean, nullable=False, server_default=db.text("false"))
    EPF = db.Column(db.Boolean, nullable=False, server_default=db.text("false"))
    Tour = db.Column(db.Boolean, nullable=False, server_default=db.text("false"))
    ReleaseDate = db.Column(db.Date, nullable=False, server_default=db.text("now()"))
