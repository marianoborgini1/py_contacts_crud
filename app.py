import os
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, request, redirect, url_for, session
from models.database import db

from models.table_user import User
from models.table_contacts import Contactos
from routes.auth import rout_auth
from routes.contacts import rout_contacts

app = Flask(__name__)

# Leemos la URL y corregimos el clásico error "postgres://" si llega a estar mal escrito
url_db = os.environ.get('DATABASE_URL')
if url_db and url_db.startswith("postgres://"):
    url_db = url_db.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = url_db
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    "pool_pre_ping": True,
    "pool_recycle": 300,
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default_key_flask')

db.init_app(app)

# ¡MAGIA!: BORRAMOS EL db.create_all() PARA QUE VERCEL NO EXPLOTE POR TIEMPO

app.register_blueprint(rout_auth)
app.register_blueprint(rout_contacts)

@app.route('/')
def index():
    if 'userId' in session:
        return redirect(url_for('contacts.dashboard'))
    return render_template('index.html')

# CREA LAS TABLAS MANUALMENTE (table secret)
@app.route('/setup-db')
def setup_db():
    try:
        db.create_all()
        return "<h1>✅ TABLAS CREADAS Y BASE DE DATOS CONECTADA PERFECTAMENTE</h1>"
    except Exception as e:
        return f"<h1>🚨 ERROR AL CONECTAR CON NEON:</h1><p>{str(e)}</p>"

if __name__ == "__main__":
    app.run(debug=True)