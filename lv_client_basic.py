#!/usr/bin/python
#*** encoding:utf-8 ***

# This file is part of La Vida
# Copyright (C) 2011 Florian R. A. Angermeier
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

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
