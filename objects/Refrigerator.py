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

import gameEngine
from gameEngine.Object import Object

class Refrigerator( object ):
    def __init__( self, id, x, y, z ):
        self.id = id
        self.type = 'Refrigerator'
        self.pos = [ x, y, z ]
        self.radii = { 'drink': 1,
                       'eatSnack': 1 }
        self.isInUse = False

    def drink( self, user ):
        # The user drinks somthing.
        # print 'DEBUG: %s.%s is called.' % ( __name__, dir( self ) )
        user.increaseNeed( 'water', 1.388888889 )

    def eatSnack( self, user ):
        # The user eats a snack.
        # print 'DEBUG: %s.%s is called.' % ( __name__, dir( self ) )
        user.increaseNeed( 'food', 0.555555556 )
