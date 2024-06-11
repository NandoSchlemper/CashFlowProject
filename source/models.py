from source import db

class roles:
    ADM = "Administrator"
    FIN = "Finantial"
    OPE = "Operational"
    HR  = "Human Resources"
    ALM = "Warehouse"


class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(55), nullable=False)
    email = db.Column(db.String(55), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    role = db.Column(db.Enum(roles), nullable=False)

    def get_id(self):
        self.uid

