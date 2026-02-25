import os
import traceback
from flask import Flask

# Envolvemos TODO en un bloque try para que no se escape ningún error
try:
    from dotenv import load_dotenv
    load_dotenv()

    from flask import render_template, request, redirect, url_for, flash, session
    from models.database import db
    from models.table_user import User
    from models.table_contacts import Contactos
    from routes.auth import rout_auth
    from routes.contacts import rout_contacts

    app = Flask(__name__)

    # Obtenemos la URL y forzamos a que empiece con postgresql:// (Clásico error de Vercel/Neon)
    url_db = os.environ.get('DATABASE_URL')
    if url_db and url_db.startswith("postgres://"):
        url_db = url_db.replace("postgres://", "postgresql://", 1)

    app.config['SQLALCHEMY_DATABASE_URI'] = url_db
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {"pool_pre_ping": True, "pool_recycle": 300}
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default_key_flask')

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(rout_auth)
    app.register_blueprint(rout_contacts)

    @app.route('/')
    def index():
        if 'userId' in session:
            return redirect(url_for('contacts.dashboard'))
        return render_template('index.html')

except Exception as e:
    # SI ALGO EXPLOTA (Importaciones, base de datos, etc)
    # Creamos una "App de Emergencia" solo para mostrar el error en la web
    app = Flask(__name__)
    error_exacto = traceback.format_exc()
    
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def atrapar_todo(path):
        return f"""
        <div style="font-family: sans-serif; padding: 20px;">
            <h1 style="color: red;">🚨 ERROR CRÍTICO AL INICIAR FLASK:</h1>
            <p>Vercel está intentando arrancar pero chocó contra esto:</p>
            <pre style="background: #222; color: #0f0; padding: 15px; border-radius: 5px; overflow-x: auto;">{error_exacto}</pre>
            <p><b>URL cargada en memoria:</b> {os.environ.get('DATABASE_URL')}</p>
        </div>
        """

if __name__ == "__main__":
    app.run(debug=True)