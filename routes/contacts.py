from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash, session
from pprint import pprint #permite mostrar datos complejos de forma facil de leer en consola
from models.database import db
from models.table_user import User
from models.table_contacts import Contactos


rout_contacts = Blueprint('contacts', __name__)

@rout_contacts.route("/dashboard", methods=["GET", "POST"]) # get metodo por defecto para recuperar una representacion de un recurso especifico, no es discreto, sirve para enviar informacion al servidor por url
def dashboard():
    if 'userId' not in session:
        flash("Por favor, iniciá sesión para acceder.")
        return redirect(url_for('auth.login'))
    
    if request.method=="POST":            
        nombre = request.form["nombre"]
        telefono = request.form["telefono"]
        email = request.form["email"]

        newContacto = Contactos(nombre=nombre, telefono=telefono, email=email, id_user=session['userId'])

        db.session.add(newContacto)
        db.session.commit()

        pprint(request.form) # se muestra lo que puso el usuario
        flash("Contacto aregado correctamente!")
        return redirect(url_for('contacts.dashboard'))
    else:
        readContacto = Contactos.query.filter_by(id_user=session['userId']).all()
        return render_template("dashboard.html", listDate = readContacto) # returna el formulario vacio
    
@rout_contacts.route("/delete/<int:id>")
def deleteContacto(id):
    
    #busca contacto en la db si no existe devuelve ERROR 404
    contactoDelete = Contactos.query.get_or_404(id)
    
    #borrar de la db
    db.session.delete(contactoDelete)
    db.session.commit()
    
    #vuelve a pagina del formulario
    return redirect(url_for('contacts.dashboard'))

@rout_contacts.route("/update/<int:id>", methods=["GET", "POST"])
def updateContacto(id):
    if request.method == "POST":
        contactoUpdate = Contactos.query.get_or_404(id)
        
        contactoUpdate.nombre = request.form['nombre']
        contactoUpdate.telefono = request.form['telefono']
        contactoUpdate.email = request.form['email']
        
        db.session.commit()
        
        flash("Se actualizo el contacto correctamente!")
        return redirect(url_for('contacts.dashboard'))
    else:
        contactoUpdate = Contactos.query.get_or_404(id)
        return render_template("update.html", contacto = contactoUpdate)
        