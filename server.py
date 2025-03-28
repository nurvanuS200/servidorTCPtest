import socket

def start_server():
    #configuración
    host = '127.0.0.1'  # localhost
    port = 5000         # puerto a escuchar

    """creando socket:
        - AF_INET: familia de direcciones para IPv4
        - SOCK_STREAM: tipo de socket para conexiones TCP """
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind((host, port))
    servidor_socket.listen(10)  # se puede escuchar hasta 10 conexiones
    print(f"Servidor escuchando en {host}:{port}...")

    while True:
        # acepta una conexión entrante
        conn, addr = servidor_socket.accept()
        print(f"Conexión establecida con {addr}")

        while True:
            # recibir datos del cliente
            datos = conn.recv(1024).decode('utf-8')
            if not datos:
                break

            print(f"Mensaje recibido: {datos}")

            # si el mensaje es "DESCONEXION", cerrar la conexión con el cliente
            if datos.upper() == "DESCONEXION":
                print("Cliente solicitó desconexión.")
                conn.close()
                break
            else:
                # devolver el mensaje pero en mayúsculas
                respuesta = datos.upper()
                conn.sendall(respuesta.encode('utf-8'))

if __name__ == "__main__":
     # iniciando servidor
    start_server() 
