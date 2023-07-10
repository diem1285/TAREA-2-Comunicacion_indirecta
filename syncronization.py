#importa las bibliotecas
import subprocess
import os
import shutil
import time
import hashlib
import logging
####rutas de los nodos

leader_directory = '/ruta/nodo/leader/'
follower_directories = ['/ruta/nodo/follower1', '/ruta/nodo/follower2']

################
#funcion para sincronizar los archivos desde el nodo líder a los nodos seguidores utilizando rsync

def sync_files():
    for follower_dir in follower_directories:
        subprocess.call(['rsync', '-avz', leader_directory + '/', follower_dir])

################
#bucle continuo

while True:
    sync_files()  # Sincroniza los archivos

##########################################################################


#def calculate_file_hash(file_path):
#    """
#    Calcula el hash de un archivo dado.
#    """
#    hasher = hashlib.md5()
#    with open(file_path, 'rb') as file:
#        for chunk in iter(lambda: file.read(4096), b''):
#            hasher.update(chunk)
#    return hasher.hexdigest()

#def check_data_sync():
#    """
#    Verifica la sincronización de datos entre los nodos líder y seguidores.
#    """
#    leader_directory = '/ruta/nodo/leader/'  # Ruta en el contenedor del nodo líder
#    follower_directories = [
#        '/ruta/nodo/follower1',  # Ruta en el contenedor del seguidor 1
#        '/ruta/nodo/follower2',  # Ruta en el contenedor del seguidor 2
#        '/ruta/al/nodo/seguidor3'   # Ruta en el contenedor del seguidor 3
#    ]

#    leader_files = os.listdir(leader_directory)
#    logger = logging.getLogger('sync_logger')
#    logger.setLevel(logging.INFO)
#    file_handler = logging.FileHandler('/ruta/archivo/sync_log.txt')  # Ruta en el contenedor para el archivo de log
#    logger.addHandler(file_handler)

#    for follower_dir in follower_directories:
#        follower_files = os.listdir(follower_dir)
#        for file in leader_files:
#            leader_file_path = os.path.join(leader_directory, file)
 #           follower_file_path = os.path.join(follower_dir, file)
 #           if file in follower_files:
 #               leader_hash = calculate_file_hash(leader_file_path)
 #               follower_hash = calculate_file_hash(follower_file_path)
 #               if leader_hash != follower_hash:
 #                   logger.error(f"La sincronización ha fallado para el archivo {file}")
 #               else:
#                    logger.info(f"La sincronización ha sido satisfactoria para el archivo {file}")
#            else:
#                logger.error(f"El archivo {file} no se ha replicado en el nodo seguidor")

# Configuración del logger
#logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Ejemplo de uso
#check_data_sync()

