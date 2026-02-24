from models.database import db

class Contactos(db.Model):
    __tablename__ = 'contactos'
    id = db.Column(db.Integer, primary_key = True)
    
    # Conexion con el usuario dueño
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    nombre = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100))
