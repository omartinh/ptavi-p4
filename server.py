#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    c_dicc = {}

    def handle(self):
       
       
        self.wfile.write(b"Hemos recibido tu peticion")
        c_a_list=list(self.client_address)
        ip = c_a_list[0]
        port = c_a_list[1]
        print('IP:', ip)
        print('PORT:',  port)
        for line in self.rfile:
            print("El cliente nos manda: ", line.decode('utf-8'))

        data_list = line.decode('utf-8').split(' ')

        if data_list[0] == 'REGISTER':
            self.c_dicc[ip]=data_list[1]
            self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")

            
            
            
        

if __name__ == "__main__":
    try:
        PORT = int(sys.argv[1])
    except ValueError:
        sys.exit('No integer value')
    serv = socketserver.UDPServer(('', PORT), SIPRegisterHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
