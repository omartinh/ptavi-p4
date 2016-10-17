#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import client


class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    def client_address(self):
        return(client.IP & client.PORT)

    def handle(self):
        self.wfile.write(b"Hemos recibido tu peticion") 
        for line in self.rfile: # rfile lee el fichero
            print(client_address())
            print("El cliente nos manda: ", line.decode('utf-8')) # codificamos los bytes, de la linea q leemos

if __name__ == "__main__":
    serv = socketserver.UDPServer(('', 6001), EchoHandler)  # tupla-->('',6001) y manegador--> EchoHandler trata las peticiones
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
