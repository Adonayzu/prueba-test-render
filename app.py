from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # permite peticiones desde cualquier origen (para pruebas)

@app.route('/')
def home():
    return jsonify({
        "status": "ok",
        "mensaje": "Backend de Aragosand funcionando en Render"
    })
    
    

@app.route('/health')
def health():
    return jsonify({"health": "ok"})

@app.route('/api/saludo')
def saludo():
    return jsonify({
        "saludo": "Hola desde el backend en Render",
        "origen": "prueba-test-render (Flask)"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)