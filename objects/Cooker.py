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

class Cooker( Object ):
    def __init__( self, id, x, y, z ):
        self.id = id
        self.type = 'Cooker'
        self.pos = [ x, y, z ]
        self.radii = { 'cook': 1 }
        self.isInUse = False

    def cook( self, user ):
        # The user cooks on the cooker and eats.
        # print 'DEBUG: %s.%s is called.' % ( __name__, dir( self ) )
        user.increaseNeed( 'food', 0.37037037 )
