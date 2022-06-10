from extensions import db

class HOSTS(db.Model):

    __tablename__ = "Hosts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hostname = db.Column(db.Text, nullable=False)
    ip = db.Column(db.Text, unique=True, nullable=False)
    mac = db.Column(db.Text)
    availability = db.Column(db.Boolean)
    last_heard = db.Column(db.Text)

    def __repr__(self):
        return f"Host: {self.hostname}"
