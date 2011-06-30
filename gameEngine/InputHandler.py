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

class InputHandler:
    # A basic input handler.
    
    def __init__( self, server ):
        self.server = server
        self.cmdPrefix = '\033['
        self.cmdSeperator = ';'
        self.cmdPostfixPosition = 'H'
        self.cmdPostfixColor = 'm'
        self.cmdTab = '\t'
        self.pos = ( 48, 1 )
        self.keyPressed = ''
    
    def run( self, threadPool ):
        while( self.server.stop != True ):
            cmdPosition = '%s%i%s%i%s' % ( self.cmdPrefix, self.pos[0], self.cmdSeperator, self.pos[1], self.cmdPostfixPosition )
            self.keyPressed = raw_input( '%sLa Vida (quit): ' % ( cmdPosition ) )
            if( self.keyPressed.lower() == 'quit' ):
                self.server.stop = True
