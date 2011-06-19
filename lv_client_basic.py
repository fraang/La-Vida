#!/usr/bin/python
#*** encoding:utf-8 ***

from twisted.internet import reactor, protocol

from lv_protocol import lv_protocol

class lv_clientFactory( protocol.ClientFactory ):
	protocol = lv_protocol

class lv_client:
	def __init__( self ):
		reactor.callInThread( self.runInterface )
		reactor.connectTCP( raw_input( '\033[1;37mlv_client_basic\033[0m host [127.0.0.1] > ' ), 65000, lv_clientFactory() )
		reactor.run()
		
	def runInterface( self ):
		playerInput = ''
		while( playerInput != 'quit' ):
			playerInput = raw_input( '\033[1;37mlv_client_basic\033[0m command > ' )

if( __name__ == '__main__' ):
	client = lv_client()
