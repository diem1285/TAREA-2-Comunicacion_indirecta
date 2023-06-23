import pika
import atexit
import json


# Configuración de RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='formulario_queue')

def enviar_formulario(formulario):
    # Convertir formulario a JSON
    formulario_json = json.dumps(formulario)

    # Publicar formulario en la cola de mensajes
    channel.basic_publish(exchange='', routing_key='formulario_queue', body=formulario_json)

    print('Formulario enviado correctamente a la cola de mensajes.')

# Cerrar la conexión de RabbitMQ al finalizar
atexit.register(connection.close)
