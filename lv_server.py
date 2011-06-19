#!/usr/bin/python
#*** encoding:utf-8 ***

from twisted.internet import reactor

import gameEngine
from gameEngine.lv_serverFactory import lv_serverFactory
from gameEngine.lv_world import lv_world

class lv_server:
	def __init__( self ):
		# Initializing the simulation
		self.world = lv_world( 1 )
	def run( self ):
		print 'Server \033[34mI\033[0m Starting world thread...'
		reactor.callInThread( self.world.run )

		print 'Server \033[34mI\033[0m Starting listening socket...'
		reactor.listenTCP( 65000, lv_serverFactory() )

		print 'Server \033[34mI\033[0m Starting reactor...'
		reactor.run()

if( __name__ == '__main__' ):
	server = lv_server()
	server.run()
