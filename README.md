# 📇 PyContacts - Gestor de Contactos Web

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

## 📌 Sobre el Proyecto

**PyContacts** es una aplicación web de gestión de contactos desarrollada completamente en Python utilizando el micro-framework Flask. 

Este es un proyecto de aprendizaje personal diseñado con el objetivo de consolidar **fundamentos sólidos sobre el desarrollo Backend**. La meta principal fue entender a fondo el ciclo de vida de una petición HTTP, el enrutamiento (Routing), la integración con bases de datos relacionales en la nube y la separación de responsabilidades usando el patrón Modelo-Vista-Controlador (MVC).

## 🚀 Características Principales (CRUD)

El sistema permite gestionar una agenda de manera intuitiva, ejecutando las cuatro operaciones fundamentales de persistencia de datos, sumado a un sistema de autenticación:

* **Autenticación Segura:** Registro, inicio de sesión y recuperación de contraseñas mediante tokens enviados por email.
* **Create (Crear):** Registro de nuevos contactos asociados únicamente al usuario logueado, con validación de campos.
* **Read (Leer):** Visualización en tiempo real de todos los contactos almacenados en la base de datos privada del usuario.
* **Update (Actualizar):** Modificación de los datos (Nombre, Teléfono, Email) de un contacto existente.
* **Delete (Eliminar):** Borrado seguro de registros con alertas dinámicas de confirmación.

## 🛠️ Tecnologías Utilizadas

* **Backend:** Python 3, Flask.
* **ORM:** Flask-SQLAlchemy (para la gestión y mapeo de la base de datos).
* **Base de Datos:** PostgreSQL alojado en Neon (Serverless Database).
* **Seguridad:** Werkzeug (hashing de contraseñas) e ItsDangerous (generación de tokens para recuperación de cuentas).
* **Frontend:** HTML5, CSS3 nativo (diseño responsive, sin frameworks pesados), Jinja2 (Motor de plantillas).
* **Interactividad:** SweetAlert2 para alertas dinámicas y confirmaciones de acciones.

## 🗄️ Estructura de la Base de Datos (DER)

El proyecto utiliza una estructura relacional de **1 a Muchos (1:N)** gestionada mediante PostgreSQL y SQLAlchemy. La base de datos consta de dos tablas principales vinculadas:

1. **Tabla `User`:**
   * `id`: Integer (Primary Key, Auto-incrementable)
   * `username`: String (Not Null)
   * `email`: String (Unique, Not Null)
   * `password`: String (Not Null)

2. **Tabla `Contactos`:**
   * `id`: Integer (Primary Key, Auto-incrementable)
   * `id_user`: Integer (Foreign Key -> `User.id`, Not Null)
   * `nombre`: String (Not Null)
   * `telefono`: String (Not Null)
   * `email`: String (Opcional)

*Nota: La clave foránea `id_user` garantiza que cada usuario acceda de forma exclusiva y privada únicamente a los contactos que él mismo registró.*

## 🔗 Link de la web para probar
<https://marianoborgini.pythonanywhere.com/>

## 💻 Instalación y Uso Local

Si querés clonar el proyecto y correrlo en tu máquina local, seguí estos pasos:

1. Cloná el repositorio:
```bash
   git clone [https://github.com/marianoborgini1/py_contacts_crud.git](https://github.com/marianoborgini1/py_contacts_crud.git)
```
2. Creá un archivo .env en la raíz del proyecto y configurá tus credenciales (Base de datos Neon y cuenta de Gmail para envíos de tokens).
   
4. Instalá las dependencias del proyecto:
``` Bash
   pip install -r requirements.txt
```
4. Abrí una terminal y ejecutá el servidor en tu máquina:
```bash
   python app.py
```


