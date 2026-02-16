from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Contactos(db.Model):
    __tablename__ = 'contactos'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100))
