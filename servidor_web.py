from flask import Flask, render_template, request
from cola_mensajes import enviar_formulario

app = Flask(__name__)

#@app.route('/generar_formulario', methods=['POST'])
@app.route("/")
def generar_formulario():
    # Generar formulario aleatorio
    formulario = {
        'nombre': 'John Doe',
        'edad': 30,
        'direccion': '123 Main St',
        # Agrega más campos según tus necesidades
    }

    # Enviar formulario a la cola de mensajes
    enviar_formulario(formulario)

    return 'Formulario generado y enviado correctamente.'

if __name__ == '__main__':
    app.run(host="192.168.100.44", port=8003,debug=True)


