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
