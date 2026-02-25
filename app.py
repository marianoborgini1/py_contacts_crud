from flask import Flask

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def prueba_de_vida(path):
    return "<h1>✅ ¡VERCEL ESTÁ VIVO! El problema está en los modelos o las rutas.</h1>"