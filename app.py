import os       
from dotenv import load_dotenv             
load_dotenv()                              

from flask import Flask, render_template, request, redirect, url_for, flash, session
from pprint import pprint
from models.database import db
from models.table_user import User
from models.table_contacts import Contactos

from routes.auth import rout_auth
from routes.contacts import rout_contacts

app = Flask(__name__)

# Llama a la URL de la base de datos desde el .env por seguridad
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    "pool_pre_ping": True,
    "pool_recycle": 300,
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Llama a la clave desde el .env 
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default_key_flask')

#conexion le decimos que esta es nuestra app
db.init_app(app)

# VARIABLE PARA ATRAPAR EL ERROR
error_db = None

# Intentamos crear la tabla. Si explota, guardamos el error en vez de romper la página
try:
    with app.app_context():
        db.create_all()
except Exception as e:
    error_db = str(e)
    
# Registro de rutas 
app.register_blueprint(rout_auth)
app.register_blueprint(rout_contacts)

@app.route('/')
def index():
    # SI HUBO UN ERROR, LO MOSTRAMOS GIGANTE EN LA PANTALLA:
    if error_db:
        url_cargada = os.environ.get('DATABASE_URL')
        return f"<h1>🚨 REPORTE DE ERROR:</h1><p><b>Motivo exacto:</b> {error_db}</p><p><b>¿Vercel está leyendo la URL?:</b> {url_cargada}</p>"
        
    # Si tiene sesión iniciada redirige al dashboard
    if 'userId' in session:
        return redirect(url_for('contacts.dashboard'))
        
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)