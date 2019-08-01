#!/usr/bin/env python

from twisted.internet import protocol, reactor
from time import ctime

PORT = 21567

class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print('...connected from:', clnt)

    def dataReceived(self, data):
        # self.transport.write('[%s] %s' % (ctime(), data))
        self.transport.write( bytes('[%s] %s' % (ctime(), data.decode('utf-8')) , 'utf-8') )


factory = protocol.Factory()
factory.protocol = TSServProtocol
print('waiting for connection...')
reactor.listenTCP(PORT, factory)
reactor.run()


