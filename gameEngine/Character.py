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

from random import choice

from Brain import Brain

class Character:
    def __init__( self, id, world, gender ):
        self.world = world              # The world a character belongs to.
        self.id = id                    # Unique integer number to identify a character.
        self.pos = [ 1, 1, 0 ]          # A characters current position.
        self.destination = [ 1, 1, 0 ]  # A characters destination for movement.
        self.radii = { 'talk': 1 }

        if( gender.lower() == 'random' ):                   # A characters gender.
            self.gender = choice( ( 'male', 'female' ) )    #
        else:                                               #
            self.gender = gender                            #
            
        # The brain which provides attributes and methodes for the ai of a character.
        self.brain = Brain( self )                                                                                                                                                          # near the character or object.

        self.needs = { 'sleep':     500,    # The chracters needs.
                       'food':      500,    #
                       'water':     500,    #
                       'urination': 500,    #
                       'hygiene':   500,    #
                       'fun':       500,    #
                       'social':    500 }   #

    def teleportTo( self, x, y, z ):
        # print 'DEBUG: Character %i teleports to X: %i Y: %i Z: %i.' % ( self.id, x, y, z )
        self.pos = [ x, y, z ]

    def goTo( self, x, y, z ):
        # print 'DEBUG: Character %i goes to X: Y: %i %i Z: %i.' % ( self.id, x, y, z )
        self.destination = [ x, y, z ]

    def move( self ):
        # X axis
        if( self.pos[ 0 ] != self.destination[ 0 ] ):
            # print 'DEBUG: Character %i is on his/her way on the x axis.'
            if( self.pos[ 0 ] < self.destination[ 0 ] ):
                self.pos[ 0 ] += 1
            elif( self.pos[ 0 ] > self.destination[ 0 ] ):
                self.pos[ 0 ] -= 1
        # Y axis
        if( self.pos[ 1 ] != self.destination[ 1 ] ):
            # print 'DEBUG: Character %i is on his/her way on the y axis.'
            if( self.pos[ 1 ] < self.destination [ 1 ] ):
                self.pos[ 1 ] += 1
            elif( self.pos[ 1 ] > self.destination[ 1 ] ):
                self.pos[ 1 ] -= 1
        # Z axis
        if( self.pos[ 2 ] != self.destination[ 2 ] ):
            # print 'DEBUG: Character %i is on his/her way on the z axis.'
            if( self.pos[ 2 ] < self.destination [ 2 ] ):
                self.pos[ 2 ] += 1
            elif( self.pos[ 2 ] > self.destination[ 2 ] ):
                self.pos[ 2 ] -= 1
                
    def increaseNeed( self, needName, needValue ):
        try:
            if( self.needs[needName] < 1000 ):
                self.needs[needName] += needValue
            elif( self.needs[needName] != 1000 ):
                self.needs[needName] = 1000
        except:
            pass

    def decreaseNeeds( self ):
        try:
            if( self.brain.activity != 'rest' and self.brain.activity != 'sleep' ):
                self.needs['sleep'] -= 0.011574074
            if( self.brain.activity != 'cook' ):
                self.needs['food'] -= 0.003858025
            if( self.brain.activity != 'drink' ):
                self.needs['water'] -= 0.011574074
            if( self.brain.activity != 'use' ):
                self.needs['urination'] -= 0.069444444
            if( self.brain.activity != 'shower' ):
                self.needs['hygiene'] -= 0.005787037
            if( self.brain.activity != 'watch' ):
                self.needs['fun'] -= 0.034722222
            if( self.brain.activity != 'talk' ):
                self.needs['social'] -= 0.011574074
        except:
            pass

    def processActivity( self ):
        # Process the activity of a character.
        if( self.brain.activityTimer > 0 ):
            try:
                if( self.brain.isInRange( self.brain.activityInteractive, self.brain.activity ) ):
                    # print '\033[32mInfo\033[0m Character %i: Character or object with id %i is in range.' % ( self.id, self.brain.activityInteractive.id )
                    # print '\033[32mInfo\033[0m Character %i interacts with the object of type %s.' % ( self.id, self.brain.activityInteractive.type )
                    exec 'self.brain.activityInteractive.%s( self )' % ( self.brain.activity )                                                                                                                                        # modify a character attribute.
                    self.brain.activityTimer -= 1
                else:
                    # print '\033[32mInfo\033[0m Character %i: Character or object with id %i is in range.' % ( self.id, self.brain.activityInteractive.id )
                    self.goTo( self.brain.activityInteractive.pos[0], self.brain.activityInteractive.pos[1], self.brain.activityInteractive.pos[2] )
                    self.move()
            except:
                print '\033[31mError\033[0m Character %i: Interactive does not exist.' % ( self.id )
        else:
            self.brain.getNextActivity()
            
    def talk( self, opposite):
        # The opposite talks to this character.
        # print 'DEBUG: %s.%s is called.' % ( __name__, dir( self ) )
        opposite.increaseNeed( 'social', 0.277777778 )
