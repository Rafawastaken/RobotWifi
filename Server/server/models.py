from server import db

class RobotModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String, unique = True, nullable = False)
    estado = db.Column(db.Integer, unique = False, nullable = False, default = 0)

db.create_all()