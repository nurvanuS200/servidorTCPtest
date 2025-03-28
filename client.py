import socket

def start_client():
    host = '127.0.0.1'  # localhost
    port = 5000          # puerto del servidor

    # socket
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect((host, port))
    print(f"Conexión establecida con el servidor en {host}:{port}")

    while True:
        mensaje = input("Ingresa un mensaje para enviar al servidor: ") # solicita mensaje al usuario
        cliente_socket.sendall(mensaje.encode('utf-8')) # envia mensaje al servidor

        # si el mensaje es "DESCONEXION", cierra la conexión
        if mensaje.upper() == "DESCONEXION":
            print("Desconectando del servidor...")
            cliente_socket.close()
            break

        # recibe y muestra la respuesta del servidor
        respuesta = cliente_socket.recv(1024).decode('utf-8')
        print(f"Respuesta del servidor: {respuesta}")

if __name__ == "__main__":
    start_client()
