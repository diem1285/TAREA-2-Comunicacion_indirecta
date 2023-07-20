import socket

# Dirección IP y puerto del líder
leader_node = "zookeeper-leader"
leader_port = 8282

def recibir_archivo(archivo, puerto):
    try:
        # Crear un socket TCP para la comunicación con el líder
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Enlazar el socket al puerto para recibir el archivo
            sock.bind(("0.0.0.0", puerto))
            sock.listen()

            print(f"Esperando conexión del líder en el puerto {puerto}...")
            conn, addr = sock.accept()

            with open(archivo, "wb") as f:
                # Recibir el contenido del archivo del líder
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    f.write(data)

            print("Archivo recibido con éxito del líder.")

    except Exception as e:
        print(f"Error al recibir el archivo del líder: {e}")

if __name__ == "__main__":
    # Recibir el archivo del líder en el seguidor zookeeper-follower1-1
    recibir_archivo("/ruta/del/archivo-en-seguidor.txt", leader_port)
