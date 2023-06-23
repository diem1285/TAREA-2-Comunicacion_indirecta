import pika
import json
import os

# Configuración de RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='formulario_queue')

def procesar_formulario(ch, method, properties, body):
    # Decodificar formulario JSON
    formulario = json.loads(body)

    # Realizar validación y deduplicación
    # ...

    # Guardar formulario en un archivo local
    with open('formulario.json', 'w') as file:
        json.dump(formulario, file)

    print('Formulario procesado y guardado localmente.')

# Configuración de RabbitMQ para recibir mensajes
channel.basic_consume(queue='formulario_queue', on_message_callback=procesar_formulario, auto_ack=True)

# Iniciar el bucle de RabbitMQ para recibir mensajes
channel.start_consuming()
