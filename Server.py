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

import os
from time import sleep
from twisted.internet import reactor

import gameEngine
from gameEngine.ServerFactory import ServerFactory
from gameEngine.InputHandler import InputHandler
from gameEngine.World import World

import asciiWidgets
from asciiWidgets.AsciiUI import AsciiUI

class Server:
    def __init__( self ):
        self.stop = False
        self.threadPool = None
        self.world = World( self, 2 )
        self.inputHandler = InputHandler( self )
        self.asciiUI = AsciiUI( self, self.world )
    
    def quitLoop( self ):
        while( self.stop == False ):
            sleep( 0.1 )
        reactor.stop()
        
    def run( self ):
        self.threadPool = reactor.getThreadPool()
        
        print '\033[32mInfo\033[0m Starting world thread...'
        reactor.callInThread( self.world.run, self.threadPool )
        
        print '\033[32mInfo\033[0m Starting input handler thread...'
        reactor.callInThread( self.inputHandler.run, self.threadPool )
        
        print '\033[32mInfo\033[0m Starting ASCII UI thread...'
        reactor.callInThread( self.asciiUI.run, self.threadPool )

        reactor.callLater( 1, self.quitLoop )

        print '\033[32mInfo\033[0m Starting listening socket...'
        reactor.listenTCP( 65000, ServerFactory() )
        
        print '\033[32mInfo\033[0m Starting reactor...'
        reactor.run()
        
if( __name__ == '__main__' ):
    Server = Server()
    Server.run()
    os.system( 'clear' )
