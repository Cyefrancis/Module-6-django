"""
¿Qué facilidades nos proporciona Django?
Es rapido, es seguro, escalable y versatil

Con relación al levantamiento de un servidor. ¿Existe una forma de realizarlo con Python y sin Django?
si se puede haciendo uso de modulos integrados como http.server y socketserver

¿Qué desventajas nos trae este tipo de proyectos sin Django?
sirve mas para hacer pruebas simples pero son poco escalables para realizar apps web mas complejas 
"""


# este es lo que se pide en Levante un servidor utilizando Python. Debe basarse en el ejercicio realizado en las capsulas. Muestre un
# mensaje que indique “Servidor levantado mediante http.server”.
import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT),Handler) as httpd :
    print("Servidor levantado mediante http.server", PORT)
    httpd.serve_forever()

#para ejecutar esto se hace desde consola "python leer.py" 