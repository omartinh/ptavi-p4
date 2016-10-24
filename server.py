#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import json
import time


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """
    c_dicc = {}

    def handle(self):
       
        c_attr = {}
       
        self.json2registered()
        self.wfile.write(b"Hemos recibido tu peticion ")
        c_a_list=list(self.client_address)
        ip = c_a_list[0]
        port = c_a_list[1]
        print('IP:', ip)
        print('PORT:',  port)

        for line in self.rfile:
            print("El cliente nos manda: ", line.decode('utf-8'))

        data_list = line.decode('utf-8').split(' ')

        if data_list[0].upper() == 'REGISTER':

            usuario=data_list[1]
            self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
            expires = time.gmtime(time.time() + int(data_list[2]))
            c_attr['address'] = ip
            if int(data_list[2]) == 0:
                del self.c_dicc[Usuario]
                self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
            elif int(data_list[2]) > 0 :
               self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
               c_attr['expires']=time.strftime('%Y-%m-%d %H:%M:%S', expires)
               self.c_dicc[usuario]=c_attr
            else:
                print("Usage: client.py ip puerto register sip_address expires_value")

        """
         TRATAMOS LA CADUCIDAD DE LOS USUARIOS
        """

        Time = time.gmtime(time.time())

        try:
            
            for client in self.c_dicc:
                attr = self.c_dicc[client]   
                if Time >= time.strptime(attr['expires'], '%Y-%m-%d %H:%M:%S'):
                    del self.c_dicc[client]
        except:
            pass

        self.register2json()
            

    def register2json(self):

        fichj = open('registered.json', 'w')
        json.dump(self.c_dicc, fichj, sort_keys=True, indent=4, separators=(',', ':'))
        fichj.close()


    def json2registered(self):
        try:
            fich = open('registered.json', 'r')
            self.c_dicc = fich.load(fich)
            fich.close()
        except:
            self.c_dicc = {}



if __name__ == "__main__":

    try:
        PORT = int(sys.argv[1])
    except ValueError:
        sys.exit('No integer value')

    serv = socketserver.UDPServer(('', PORT), SIPRegisterHandler)
    print("Lanzando servidor SIP...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
