# 📇 PyContacts - Gestor de Contactos Web

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

## 📌 Sobre el Proyecto

**PyContacts** es una aplicación web de gestión de contactos desarrollada completamente en Python utilizando el micro-framework Flask. 

Este es un proyecto de aprendizaje personal diseñado con el objetivo de consolidar **fundamentos sólidos sobre el desarrollo Backend**. La meta principal fue entender a fondo el ciclo de vida de una petición HTTP, el enrutamiento (Routing), la integración con bases de datos relacionales y la separación de responsabilidades usando el patrón Modelo-Vista-Controlador (MVC).

## 🚀 Características Principales (CRUD)

El sistema permite gestionar una agenda de manera intuitiva, ejecutando las cuatro operaciones fundamentales de persistencia de datos:

* **Create (Crear):** Registro de nuevos contactos con validación de campos.
* **Read (Leer):** Visualización en tiempo real de todos los contactos almacenados en la base de datos.
* **Update (Actualizar):** Modificación de los datos (Nombre, Teléfono, Email) de un contacto existente.
* **Delete (Eliminar):** Borrado seguro de registros con alertas de confirmación.

## 🛠️ Tecnologías Utilizadas

* **Backend:** Python 3, Flask.
* **Base de Datos:** SQLite (ligera y contenida en el propio proyecto).
* **Frontend:** HTML5, CSS3 nativo (diseño responsive, sin frameworks pesados), Jinja2 (Motor de plantillas).
* **Interactividad:** SweetAlert2 para alertas dinámicas y confirmaciones de acciones.

## 🗄️ Estructura de la Base de Datos

El sistema utiliza una única tabla `contactos` gestionada mediante SQLite, con la siguiente estructura:

* `id`: Integer (Primary Key, Auto-incrementable)
* `nombre`: String (Not Null)
* `telefono`: String (Not Null)
* `email`: String (Opcional)

## 🔗 Link de la web para probar
<https://marianoborgini.pythonanywhere.com/>

## 💻 Instalación y Uso Local

Si querés clonar el proyecto y correrlo en tu máquina local, seguí estos pasos:

1. Cloná el repositorio:
   ```bash

   git clone [https://github.com/marianoborgini1/py_contacts_crud.git](https://github.com/marianoborgini1/py_contacts_crud.git)

2. Instala **requirements.txt**, abri una terminal y escribi **python app.py** para crear el servidor y ejecutarlo en tu maquina.



