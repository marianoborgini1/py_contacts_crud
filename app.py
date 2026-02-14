from flask import Flask, render_template, request, redirect, url_for, flash
from pprint import pprint #permite mostrar datos complejos de forma facil de leer en consola
from models.table_contacts import db, Contactos

#flash mensaje temporal entre una pagina y otra ej: contraseña incorrecta, agregado correctamente, etc.

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contactos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#conexion le decimos que esta es nuestra app
db.init_app(app)

#creamos tabla
with app.app_context():
    db.create_all()
    
app.secret_key = "security_key_crud_contact_borgini"


@app.route("/", methods=["GET", "POST"]) # get metodo por defecto para recuperar una representacion de un recurso especifico, no es discreto, sirve para enviar informacion al servidor por url
def form():
    if request.method=="POST":            
        nombre = request.form["nombre"]
        telefono = request.form["telefono"]
        email = request.form["email"]

        newContacto = Contactos(nombre=nombre, telefono=telefono, email=email)

        db.session.add(newContacto)
        db.session.commit()

        
        pprint(request.form) # se muestra lo que puso el usuario
        flash("Contacto aregado correctamente!")
        return redirect(url_for('form'))
    else:
        readContacto = Contactos.query.all()
        return render_template("index.html", listDate = readContacto) # returna el formulario vacio

@app.route("/delete/<int:id>")
def deleteContacto(id):
    
    #busca contacto en la db si no existe devuelve ERROR 404
    contactoDelete = Contactos.query.get_or_404(id)
    
    #borrar de la db
    db.session.delete(contactoDelete)
    db.session.commit()
    
    #vuelve a pagina del formulario
    return redirect(url_for('form'))

@app.route("/update/<int:id>", methods=["GET", "POST"])
def updateContacto(id):
    if request.method == "POST":
        contactoUpdate = Contactos.query.get_or_404(id)
        
        contactoUpdate.nombre = request.form['nombre']
        contactoUpdate.telefono = request.form['telefono']
        contactoUpdate.email = request.form['email']
        
        db.session.commit()
        
        flash("Se actualizo el contacto correctamente!")
        return redirect(url_for('form'))
    else:
        contactoUpdate = Contactos.query.get_or_404(id)
        return render_template("update.html", contacto = contactoUpdate)
        
if __name__ == "__main__":
    app.run(debug=True)
    
    