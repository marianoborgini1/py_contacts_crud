from werkzeug.security import generate_password_hash, check_password_hash 
from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash, session
from pprint import pprint #permite mostrar datos complejos de forma facil de leer en consola
from models.database import db
from models.table_user import User
from models.table_contacts import Contactos


# herramientas para mandar email y generar tokens seguros
import os    
import smtplib
from email.mime.text import MIMEText
from itsdangerous import URLSafeTimedSerializer

rout_auth = Blueprint('auth', __name__)

token_secret = os.environ.get('TOKEN_SECRET_KEY', 'clave_por_defecto_tokens')
generador_tokens = URLSafeTimedSerializer(token_secret)


@rout_auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method=="POST":
        email = request.form["email"]
        password = request.form["password"]
        
        # consulta si el email ingresado es = al email guardado en db 
        userFound = User.query.filter_by(email=email).first()
        
        # Se verifica si el usuario existe y si la contraseña ingresada coincide con el hash guardado
        if userFound and check_password_hash(userFound.password, password):
            # Si el usuario ingresa los datos correctamente, se le guarda el user y el id en la memoria del navegador para que dashboard entienda quien esta en la sesion
            session['userId'] = userFound.id
            session['userName'] = userFound.username 
            return redirect(url_for('contacts.dashboard'))
        
        else:
            flash("ERROR. El email o la contraseña son incorrectos. Intenta nuevamente.")
            return redirect(url_for('auth.login'))
    else:
        return render_template('login.html')

@rout_auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method== "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        # consulta si el email ingresado es = al email guardado en db 
        userFound = User.query.filter_by(email=email).first()
        
        if userFound:
            flash("ERROR. El email ya esta registrado.")
            return redirect(url_for('auth.register'))
        
        # Hasheamos la contraseña antes de guardarla en la base de datos
        password_hasheada = generate_password_hash(password)
        newUser = User(username=username, email=email, password=password_hasheada)
        
        db.session.add(newUser)
        db.session.commit()
        
        session['userId'] = newUser.id
        session['userName'] = newUser.username
        
        #muestra si se guardo un user en consola
        pprint(request.form)
        
        return redirect(url_for('contacts.dashboard'))
    else:
        return render_template('register.html')
        
@rout_auth.route('/forget-password', methods=['GET', 'POST'])
def forget_password():
    if request.method == 'POST':
        email_ingresado = request.form['email']
        
        # Consulta si el email existe en la db
        userFound = User.query.filter_by(email=email_ingresado).first()
        
        if userFound:
            # Si usuario existe, fabrica Token único usando su email
            # Salt = Etiqueta de nombre del token 
            token = generador_tokens.dumps(email_ingresado, salt='recuperar-pass')
            link_recuperacion = url_for('auth.reset_password', token=token, _external=True)
            
            email = os.environ.get('MAIL_USER')
            key_app = os.environ.get('MAIL_PASS')
            
            cuerpo_mensaje = f"Hola {userFound.username},\n\nPara restablecer tu contraseña, hacé click en el siguiente enlace. Este enlace caduca en 15 minutos por seguridad:\n\n{link_recuperacion}"
            
            mensaje = MIMEText(cuerpo_mensaje)
            mensaje['Subject'] = 'PyContacts - Recuperar Contraseña'
            mensaje['From'] = email
            mensaje['To'] = email_ingresado
            
            # Conexion a Gmail y envia correo (try/except por si falla internet)
            try:
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.login(email, key_app)
                server.send_message(mensaje)
                server.quit()
                print("Correo enviado con éxito")
            except Exception as e:
                print("Error mandando el correo:", e)
                
        flash('Si el email está registrado, te enviamos un enlace de recuperación.', 'success')
        return redirect(url_for('auth.forget_password'))
    else:
        return render_template('forget_password.html')
    
@rout_auth.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    # Desencripta token para sacar el email
    try:
        email_del_token = generador_tokens.loads(token, salt='recuperar-pass', max_age=900)
    except:
        # Si el token es viejo, trucho o alguien lo modificó, tira error y redirect.
        flash('El enlace es inválido o ya expiró. Volvé a pedirlo.', 'error')
        return redirect(url_for('auth.forget_password'))
        
    # Si el token es válido y el usuario manda el formulario con la nueva contraseña
    if request.method == 'POST':
        nueva_password = request.form['password']
        
        # Busca al usuario usando el email 
        user = User.query.filter_by(email=email_del_token).first()
        
        if user:
            # Reemplaza contraseña vieja por la nueva (hasheada), se guarda en la DB
            user.password = generate_password_hash(nueva_password)
            db.session.commit()
            
            flash('¡Excelente! Tu contraseña fue actualizada. Ya podés iniciar sesión.', 'success')
            return redirect(url_for('auth.login'))
        
        flash('Usuario no encontrado.', 'error')
        return redirect(url_for('auth.forget_password'))
            
    else:
        return render_template('reset_password.html')

@rout_auth.route('/logout')
def logout():
    session.clear()
    flash("Cerraste sesión correctamente.", "success")
    return redirect(url_for('auth.login'))