import os       
from flask import Flask, render_template, request, redirect, url_for, flash, session, redirect
from pprint import pprint #permite mostrar datos complejos de forma facil de leer en consola
from models.database import db
from models.table_user import User
from models.table_contacts import Contactos
from dotenv import load_dotenv             
load_dotenv()                              

from routes.auth import rout_auth
from routes.contacts import rout_contacts
#flash mensaje temporal entre una pagina y otra ej: contraseña incorrecta, agregado correctamente, etc.

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

#creamos tabla
with app.app_context():
    db.create_all()
    
# Registro de rutas 
app.register_blueprint(rout_auth)
app.register_blueprint(rout_contacts)

@app.route('/')
def index():
    # Si tiene sesión iniciada redirige al dashboard
    if 'userId' in session:
        return redirect(url_for('contacts.dashboard'))
        
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
    