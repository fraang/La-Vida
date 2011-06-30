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

from AsciiWidget import AsciiWidget

class GameClock( AsciiWidget ):
    def __init__( self, pos, world ):
        self.cmdPrefix = '\033['
        self.cmdSeperator = ';'
        self.cmdPostfixPosition = 'H'
        self.cmdPostfixColor = 'm'
        self.cmdTab = '\t'
        self.pos = pos
        self.world = world
        
    def printWidget( self ):
        cmdPosition = '%s%i%s%i%s' % ( self.cmdPrefix, self.pos[0], self.cmdSeperator, self.pos[1], self.cmdPostfixPosition )
        cmdColor = '%s1%s' % ( self.cmdPrefix, self.cmdPostfixColor )
        output = '%s%sGame date: %i/%i/%i%sGame time: %i:%i:%i' % ( cmdPosition, cmdColor, self.world.gameMonth, self.world.gameDay, self.world.gameYear,
                                                                self.cmdTab, self.world.gameHour, self.world.gameMinute, self.world.gameSecond )
        cmdColor = '%s0%s' % ( self.cmdPrefix, self.cmdPostfixColor )
        output += cmdColor
        print '%s' % ( output )
