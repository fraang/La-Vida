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

class MapView( AsciiWidget ):
    def __init__( self, pos, world ):
        self.cmdPrefix = '\033['
        self.cmdSeperator = ';'
        self.cmdPostfixPosition = 'H'
        self.cmdPostfixColor = 'm'
        self.cmdTab = '\t'
        self.pos = pos
        self.world = world
        self.asciiTiles = { 0: '%s33%s42%s"%s0%s' % ( self.cmdPrefix, self.cmdSeperator, self.cmdPostfixColor, self.cmdPrefix, self.cmdPostfixColor ),
                            1: '%s30%s40%s:%s0%s' % ( self.cmdPrefix, self.cmdSeperator, self.cmdPostfixColor, self.cmdPrefix, self.cmdPostfixColor ),
                            2: '%s31%s43%s#%s0%s' % ( self.cmdPrefix, self.cmdSeperator, self.cmdPostfixColor, self.cmdPrefix, self.cmdPostfixColor ),
                            3: '%s30%s44%s~%s0%s' % ( self.cmdPrefix, self.cmdSeperator, self.cmdPostfixColor, self.cmdPrefix, self.cmdPostfixColor ),
                            4: '%s30%s44%s+%s0%s' % ( self.cmdPrefix, self.cmdSeperator, self.cmdPostfixColor, self.cmdPrefix, self.cmdPostfixColor ) }
        self.asciiObject = { 'Bed': '%s1%s37%s43%sH%s0%s' % ( self.cmdPrefix, self.cmdSeperator, self.cmdSeperator, self.cmdPostfixColor, self.cmdPrefix, self.cmdPostfixColor ),
                             'Cooker': '%s1%s30%s47%s8%s0%s' % ( self.cmdPrefix, self.cmdSeperator, self.cmdSeperator, self.cmdPostfixColor, self.cmdPrefix, self.cmdPostfixColor ),
                             'Refrigerator': '%s1%s30%s47%s*%s0%s' % ( self.cmdPrefix, self.cmdSeperator, self.cmdSeperator, self.cmdPostfixColor, self.cmdPrefix, self.cmdPostfixColor ),
                             'Toilet': '%s1%s30%s47%sO%s0%s' % ( self.cmdPrefix, self.cmdSeperator, self.cmdSeperator, self.cmdPostfixColor, self.cmdPrefix, self.cmdPostfixColor ),
                             'Shower': '%s1%s30%s47%s^%s0%s' % ( self.cmdPrefix, self.cmdSeperator, self.cmdSeperator, self.cmdPostfixColor, self.cmdPrefix, self.cmdPostfixColor ),
                             'TvSet': '%s1%s30%s43%sY%s0%s' % ( self.cmdPrefix, self.cmdSeperator, self.cmdSeperator, self.cmdPostfixColor, self.cmdPrefix, self.cmdPostfixColor ) }
                            
    def printWidget( self ):
        cmdPosition = '%s%i%s%i%s' % ( self.cmdPrefix, self.pos[0], self.cmdSeperator, self.pos[1], self.cmdPostfixPosition )
        print '%sMap view' % ( cmdPosition )
        rowId = 0
        colId = 0
        for row in self.world.typeMap:
            rowId += 1
            cmdPosition = '%s%i%s%i%s' % ( self.cmdPrefix, self.pos[0] + rowId, self.cmdSeperator, self.pos[1], self.cmdPostfixPosition )
            output = '%s' % ( cmdPosition )
            for col in row:
                output += self.asciiTiles[ col ]
            print '%s' % ( output )
            
        for object in self.world.objects:
            cmdPosition = '%s%i%s%i%s' % ( self.cmdPrefix, self.pos[0] + object.pos[0], self.cmdSeperator, self.pos[1] + object.pos[1], self.cmdPostfixPosition )
            output = '%s%s' % ( cmdPosition, self.asciiObject[ object.type ] )
            print output
            
        for character in self.world.characters:
            cmdPosition = '%s%i%s%i%s' % ( self.cmdPrefix, self.pos[0] + character.pos[0], self.cmdSeperator, self.pos[1] + character.pos[1], self.cmdPostfixPosition )
            output = '%sC' % ( cmdPosition )
            print output
