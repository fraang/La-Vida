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

from GameClock import GameClock
from NeedBar import NeedBar
from ActivityBar import ActivityBar
from MapView import MapView

class AsciiUI:
    # The ASCII user interface base class which provides the drawing loop.
    
    def __init__( self, server, world ):
        self.server = server
        self.gameClock = GameClock( ( 1, 1 ) , world)
        self.needBarSleep = NeedBar( ( 2, 1 ), 'Sleep     ', world.characters[ 0 ], 'sleep' )
        self.needBarFood = NeedBar( ( 3, 1 ), 'Food      ', world.characters[ 0 ], 'food' )
        self.needBarWater = NeedBar( ( 4, 1 ), 'Water     ', world.characters[ 0 ], 'water' )
        self.needBarUrination = NeedBar( ( 2, 30 ), 'Urination ', world.characters[ 0 ], 'urination' )
        self.needBarHygiene = NeedBar( ( 3, 30 ), 'Hygiene   ', world.characters[ 0 ], 'hygiene' )
        self.needBarFun = NeedBar( ( 4, 30 ), 'Fun       ', world.characters[ 0 ], 'fun' )
        self.needBarSocial = NeedBar( ( 2, 60 ), 'Social    ', world.characters[ 0 ], 'social' )
        self.activityBar = ActivityBar( ( 5, 1 ), world.characters[ 0 ] )
        self.mapView = MapView( (6, 0), world )
        
    def run( self, treadPool ):
        os.system( 'clear' )
        while( self.server.stop != True ):
            self.gameClock.printWidget()
            self.needBarSleep.printWidget()
            self.needBarFood.printWidget()
            self.needBarWater.printWidget()
            self.needBarUrination.printWidget()
            self.needBarHygiene.printWidget()
            self.needBarFun.printWidget()
            self.needBarSocial.printWidget()
            self.activityBar.printWidget()
            self.mapView.printWidget()
            sleep( 1 )
