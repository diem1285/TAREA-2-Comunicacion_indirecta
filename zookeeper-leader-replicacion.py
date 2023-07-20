import socket

# Ruta del archivo que se va a replicar
archivo_a_replicar = "/ruta/del/archivo.txt"

# Dirección IP y puertos de los nodos seguidores
follower1_node = "zookeeper-follower4"
follower1_port = 7001

follower2_node = "zookeeper-follower3"
follower2_port = 7000

def obtener_contenido_archivo(archivo):
    try:
        # Leer el contenido del archivo desde el líder
        with open(archivo, "rb") as f:
            contenido = f.read()
        return contenido

    except Exception as e:
        print(f"Error al obtener el contenido del archivo en el líder: {e}")
        return None

def replicar_archivo(archivo, contenido, ip_destino, puerto_destino):
    try:
        # Crear un socket TCP para la comunicación con el seguidor
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Conectar al seguidor
            sock.connect((ip_destino, puerto_destino))

            # Enviar el contenido del archivo al seguidor
            sock.sendall(contenido)

    except Exception as e:
        print(f"Error al replicar el archivo en el nodo seguidor: {e}")

if __name__ == "__main__":
    # Obtener el contenido del archivo desde el líder
    contenido_archivo = obtener_contenido_archivo(archivo_a_replicar)

    if contenido_archivo:
        # Replicar el archivo en el seguidor zookeeper-follower1-1
        replicar_archivo(archivo_a_replicar, contenido_archivo, follower1_node, follower1_port)

        # Replicar el archivo en el seguidor zookeeper-follower2
        replicar_archivo(archivo_a_replicar, contenido_archivo, follower2_node, follower2_port)

