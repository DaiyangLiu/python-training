#!/usr/bin/env python

import socketserver
from time import ctime

HOST = ''
PORT = 21568
ADDR = (HOST, PORT)

class MyRequestHandler(socketserver.StreamRequestHandler):
    def handle(self):
        print('...connected from:', self.client_address)
        data = self.rfile.readline().strip()
        print(data)
        self.wfile.write(bytes('[%s] %s' % (ctime(), data.decode('utf-8')), 'utf-8'))
        # self.wfile.write(bytes('[%s] %s/n' % (
        #     ctime(), self.rfile.readline().strip()),'utf-8'))
        print('handle over')

tcpSerSock = socketserver.TCPServer(ADDR, MyRequestHandler)
print('waiting for connection...')
tcpSerSock.serve_forever()
