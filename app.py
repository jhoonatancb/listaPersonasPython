from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/personas', methods=['GET'])
def obtener_personas():
    # Generar una lista de nombres de personas
    lista_personas = ["Juan", "María", "Pedro", "Ana", "Luis"]
    
    # Convertir la lista de nombres en formato JSON y devolverla como respuesta
    return jsonify(lista_personas)

if __name__ == '__main__':
    app.run(debug=True)
