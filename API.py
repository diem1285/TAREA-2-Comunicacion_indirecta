from flask import Flask, request, jsonify

# Configuración de Flask
app = Flask(__name__)

@app.route('/api/endpoint', methods=['POST'])
def endpoint():
    try:
        data = request.json
        # Aquí puedes realizar cualquier procesamiento o lógica con el mensaje JSON recibido
        # ...

        # Ejemplo de respuesta
        response_data = {'message': '¡Mensaje recibido y procesado exitosamente!'}
        return jsonify(response_data), 200
    except Exception as e:
        error_message = {'error': str(e)}
        return jsonify(error_message), 500

if __name__ == '__main__':
    # Iniciar el servidor Flask en el puerto 8080
    app.run(host='0.0.0.0', port=8181)
