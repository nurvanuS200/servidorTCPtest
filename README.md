# Proyecto de Comunicación Cliente-Servidor en Python
Este proyecto implementa una comunicación básica entre un servidor y un cliente utilizando sockets en Python. El servidor escucha en un puerto específico y procesa mensajes enviados por el cliente, respondiendo con el mensaje en mayúsculas. La comunicación se mantiene hasta que el cliente envía el mensaje "DESCONEXION".

Estructura del proyecto

│

├── server.py      # script que implementa el servidor.

├── client.py      # script que implementa el cliente.

└── README.md  
#### Requisitos:

Python instalado

## Clona el repositorio 
1. Abre una terminal y navega al directorio donde deseas clonar el repositorio.
2. Ejecuta: git clone https://github.com/nurvanuS200/servidorTCPtest.git

## Ejecutar el servidor 
1. Abre una terminal o power shell:
![image](https://github.com/user-attachments/assets/8c834973-319f-495f-8651-557d3e797655)

2. Navega al directorio del proyecto:

opcional: Utiliza el cmdlet Get-ChildItem para ver los archivos del directorio

2.1 Ejecuta el servidor:

server: nombre del archivo del servidor 

ejemplo:

 python server.py
 
![image](https://github.com/user-attachments/assets/b148c600-a484-428c-b1b6-77e1353bab87)

2.2 Repite el proceso de abrir otra terminal o powell shell y ahora ejecuta el cliente:

client: nombre del archivo del cliente

python client.py

![image](https://github.com/user-attachments/assets/87037827-94e8-4e61-855f-d7660bc871e1)

Ejemplo en visual studio code:
![image](https://github.com/user-attachments/assets/300aff8f-7f95-4eff-a309-7732b839842e)

## Manual de pruebas
### Caso 1: Conexión establecida
1. El cliente envía un mensaje al servidor: "hola servidor".
   
2. Si la conexión fue exitosa, el servidor muestra el mensaje recibido.
   
3. El servidor envía al cliente el mismo mensaje pero en mayúsculas: "HOLA SERVIDOR".
   
![image](https://github.com/user-attachments/assets/f5a0d284-21a3-4440-b4e8-062538621abf)

### Caso 2: Desconexión
1. Cliente envía "DESCONEXION": El cliente transmite el mensaje al servidor indicando su intención de finalizar la sesión.

2. Servidor recibe y cierra la conexión:
   - El servidor, al recibir el mensaje "DESCONEXION", cierra la conexión con el cliente utilizando el método conn.close() y así libera los recursos asociados al socket y notifica al sistema operativo que la comunicación ha finalizado.

3. Cliente cierra su socket:
   - Tras enviar el mensaje, el cliente también cierra su socket con cliente_socket.close().
![image](https://github.com/user-attachments/assets/bccc5308-bc32-4d7c-a000-11f898ba8f8f)





