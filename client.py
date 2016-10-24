#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket # para abrir caminos cliente-servidor
import sys

# Constantes. Dirección IP del servidor y contenido a enviar
try:
    IP = sys.argv[1]
    PORT = int(sys.argv[2])
    LINE = sys.argv[3:]
    # sys coge 
except:
    sys.exit('Error : IP, PORT OR LINE')


# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket: # (tipo red(internet), tipo paquete(UDP))
    my_socket.connect((IP, PORT)) # se le pasa un valor que es este caso es una tupla
    print("Enviando:", ' '.join(LINE))
    my_socket.send(bytes(' '.join(LINE), 'utf-8') + b'\r\n')  # la b es de bytes
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8')) # decode pas de bytes a utf-8
print("Socket terminado.")
