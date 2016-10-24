#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket
import sys

#  Constantes. Dirección IP del servidor y contenido a enviar


try:
    IP = sys.argv[1]
    PORT = int(sys.argv[2])
    LINE = sys.argv[3:]
except:
    sys.exit('Error: IP, PORT OR LINE')

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((IP, PORT))
    print("Enviando: ", ' '.join(LINE))
    my_socket.send(bytes(' '.join(LINE), 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))
print("Socket terminado.")
