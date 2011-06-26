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
        self.pos = [ 0, 0, 0 ]          # A characters current position.
        self.destination = [ 0, 0, 0 ]  # A characters destination for movement.

        if( gender.lower() == 'random' ):                   # A characters gender.
            self.gender = choice( ( 'male', 'female' ) )    #
        else:                                               #
            self.gender = gender                            #

        self.activity = None            # A characters activity.
        self.activityTimer = 0          # How much game seconds are left for an activity.
        self.activityInteractive = None # The character or object to interact with.

        # to-do: use the new brain class for ai
        self.activityRadiusOn = 0
        self.activityRadiusNextTo = 1
        self.activityRadiusNear = 2      
        
        # The brain which provides attributes and methodes for the ai of a character.
        self.brain = Brain( self )                                                                                                                                                          # near the character or object.

        self.needs = { 'sleep':        500,     # The chracters needs.
                       'food':         500,     #
                       'water':        500,     #
                       'hygiene':      500,     #
                       'fun':          1000,    #
                       'social':       1000 }   #

    def teleportTo( self, x, y, z ):
        print 'DEBUG: Character %i teleports to X: %i Y: %i Z: %i.' % ( self.id, x, y, z )
        self.pos = [ x, y, z ]

    def goTo( self, x, y, z ):
        print 'DEBUG: Character %i goes to X: Y: %i %i Z: %i.' % ( self.id, x, y, z )
        self.destination = [ x, y, z ]

    def move( self ):
        # X axis
        if( self.pos[ 0 ] != self.destination[ 0 ] ):
            print 'DEBUG: Character %i is on his/her way on the x axis.'
            if( self.pos[ 0 ] < self.destination[ 0 ] ):
                self.pos[ 0 ] += 1
            elif( self.pos[ 0 ] > self.destination[ 0 ] ):
                self.pos[ 0 ] -= 1
        # Y axis
        if( self.pos[ 1 ] != self.destination[ 1 ] ):
            print 'DEBUG: Character %i is on his/her way on the y axis.'
            if( self.pos[ 1 ] < self.destination [ 1 ] ):
                self.pos[ 1 ] += 1
            elif( self.pos[ 1 ] > self.destination[ 1 ] ):
                self.pos[ 1 ] -= 1
        # Z axis
        if( self.pos[ 2 ] != self.destination[ 2 ] ):
            print 'DEBUG: Character %i is on his/her way on the z axis.'
            if( self.pos[ 2 ] < self.destination [ 2 ] ):
                self.pos[ 2 ] += 1
            elif( self.pos[ 2 ] > self.destination[ 2 ] ):
                self.pos[ 2 ] -= 1

    def isInRange( self, characterOrObject, type ):
        if( type == 'On' ):
            if( characterOrObject.pos[ 0 ] >= self.pos[ 0 ] - self.activityRadiusOn and characterOrObject.pos[0] <= self.pos[ 0 ] + self.activityRadiusOn ):
                if( characterOrObject.pos[ 1 ] >= self.pos[ 1 ] - self.activityRadiusOn and characterOrObject.pos[ 1 ] <= self.pos[ 1 ] + self.activityRadiusOn ):
                    if( characterOrObject.pos[ 2 ] >= self.pos[ 2 ] - self.activityRadiusOn and characterOrObject.pos[ 2 ] <= self.pos[ 2 ] + self.activityRadiusOn ):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        if( type == 'NextTo' ):
            if( characterOrObject.pos[ 0 ] >= self.pos[ 0 ] - self.activityRadiusNextTo and characterOrObject.pos[0] <= self.pos[ 0 ] + self.activityRadiusNextTo ):
                if( characterOrObject.pos[ 1 ] >= self.pos[ 1 ] - self.activityRadiusNextTo and characterOrObject.pos[ 1 ] <= self.pos[ 1 ] + self.activityRadiusNextTo ):
                    if( characterOrObject.pos[ 2 ] >= self.pos[ 2 ] - self.activityRadiusNextTo and characterOrObject.pos[ 2 ] <= self.pos[ 2 ] + self.activityRadiusNextTo ):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        if( type == 'Near' ):
            if( characterOrObject.pos[ 0 ] >= self.pos[ 0 ] - self.activityRadiusNear and characterOrObject.pos[0] <= self.pos[ 0 ] + self.activityRadiusNear ):
                if( characterOrObject.pos[ 1 ] >= self.pos[ 1 ] - self.activityRadiusNear and characterOrObject.pos[ 1 ] <= self.pos[ 1 ] + self.activityRadiusNear ):
                    if( characterOrObject.pos[ 2 ] >= self.pos[ 2 ] - self.activityRadiusNear and characterOrObject.pos[ 2 ] <= self.pos[ 2 ] + self.activityRadiusNear ):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False

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
            if( self.activity != 'rest' and self.activity != 'sleep' ):
                self.needs['sleep'] -= 0.011574074
            if( self.activity != 'cook' ):
                self.needs['food'] -= 0.003858025
            if( self.activity != 'drink' ):
                self.needs['water'] -= 0.011574074
            if( self.activity != 'shower' ):
                self.needs['hygiene'] -= 0.005787037
            if( self.activity != 'watch' ):
                self.needs['fun'] -= 1
            # if( self.activity != 'chat' ):
            #       self.needs['social'] -= 1
        except:
            pass

    def processActivity( self ):
        # Process the activity of a character.
        
        if( self.activityTimer > 0 ):                               # Character has active activity.
            print 'Character is doing activity. Timer is not zero.'
            objectFound = False
            for object in self.world.objects:                       # Search for the object to interact with.
                if( object.id == self.activityInteractive ):        # Object found in the wolrd's object list.
                    objectFound = True
                    
                    if( self.activity == 'rest' ):
                        radiusType = 'On'
                    elif( self.activity == 'sleep' ):
                        radiusType = 'On'
                    elif( self.activity == 'eatSnack' ):
                        radiusType = 'NextTo'
                    elif( self.activity == 'cook' ):
                        radiusType = 'NextTo'
                    elif( self.activity == 'drink' ):
                        radiusType = 'NextTo'
                    elif( self.activity == 'shower' ):
                        radiusType = 'On'
                    elif( self.activity == 'watch' ):
                        radiusType = 'Near'
                    else:
                        radiusType = 'Near'

                    if( self.isInRange( object, radiusType ) ):                                                     # Checks if the object is in range of the character.
                        print 'Object found to interact with and is in range (%s). Object id is %i/%i.' % ( radiusType, self.activityInteractive, object.id )
                        print 'Character interacts with the object of type %s.' % ( object.type )
                        exec 'object.%s( self )' % ( self.activity )                            # Calls the methode of an world object which                                                                                                                                        # modify a character attribute.
                        self.activityTimer -= 1

                    else:
                        print 'Object found to interact with but is not in range (%s). Object id is %i/%i.' % ( radiusType, self.activityInteractive, object.id )
                        self.goTo( object.pos[0], object.pos[1], object.pos[2] )
                        self.move()
            if( objectFound == False ):                                                                                             # Object not found in the world's object list.
                print 'Object not found to interact. Object id is %s/%i.' % ( self.activityInteractive, object.id )
                self.activity = None
                self.activityTimer = 0
                self.activityInteractive = None
        else:                                                                                                                                           # Character is free for a new activity.
            print 'Character is thinking about the next activity. Timer is zero.'
            # Getting the lowest need
            lowestNeedName  = ''
            lowestNeedValue = 1000
            for needName in self.needs.keys():
                if( self.needs.get( needName ) < lowestNeedValue ):
                    lowestNeedName  = needName
                    lowestNeedValue = self.needs.get( needName )

            print '\033[32mInfo\033[0m Lowest need: %s (%i)' % ( lowestNeedName, lowestNeedValue )

            # Searching for an character or object to raise the need
            # if( lowestNeedName == 'fun' or lowestNeedName == 'social' ):
            #       for character in self.world.characters:
            #               self.needs[lowestNeedName] = 1000
            #               # if( character. ):
            if( lowestNeedName == 'sleep' ):
                if( lowestNeedValue < 833.333333333 ):                                                          # The sleep need is not below the minimal limit.
                    for object in self.world.objects:                                                               # Search for the object to interact with.
                        if( object.type == 'Bed' ):                                                                     # Object of type bed found in the wolrd's object list.
                            if( lowestNeedValue > 208.333333333 ):                                  # The sleep need is not below the critcal limit.
                                self.activity = 'rest'
                                self.activityTimer = 900                                                        # 15 game minutes
                                self.activityInteractive = object.id
                            else:                                                                                                   # The sleep need is below the critcal limit.
                                self.activity = 'sleep'
                                self.activityTimer = 28800                                                      # 8 game hours
                                self.activityInteractive = object.id
                            if( self.isInRange( object, 'On' ) == False ):
                                self.goTo( object.pos[0], object.pos[1], object.pos[2] )
                                self.move()
                else:                                                                                                                           # The lowest need is not below the minimal limit.
                    self.activity = 'beHappy'                                                                               # Reset the activity to a standard beHappy activity.
                    self.activityTimer = 1                                                                                  # Reset the timer to 1.
                    self.activityInteractive = None                                                                 # Reset the interactive to None.
            elif( lowestNeedName == 'food' ):
                if( lowestNeedValue < 833.333333333 ):                                                          # The food need is not below the minimal limit.
                    for object in self.world.objects:                                                               # Search for the object to interact with.
                        if( object.type == 'Refrigerator' ):                                            # Object of type refrigerator found in the wolrd's object list.
                            if( lowestNeedValue > 833.333333333 ):                                  # The food need is not below the critcal limit.
                                self.activity = 'eatSnack'
                                self.activityTimer = 300                                                        # 5 game minutes.
                                self.activityInteractive = object.id
                            if( self.isInRange( object, 'NextTo' ) == False ):
                                self.goTo( object.pos[0], object.pos[1], object.pos[2] )
                                self.move()
                        elif( object.type == 'Cooker' ):                                                        # Object of type cooker found in the wolrd's object list.
                            if( lowestNeedValue > 0 ):                                                              # The food need is below the critcal limit.
                                self.activity = 'cook'
                                self.activityTimer = 900                                                        # 15 game minutes.
                                self.activityInteractive = object.id
                            if( self.isInRange( object, 'NextTo' ) == False ):
                                self.goTo( object.pos[0], object.pos[1], object.pos[2] )
                                self.move()
                else:                                                                                                                           # The lowest need is not below the minimal limit.
                    self.activity = 'beHappy'                                                                               # Reset the activity to a standard beHappy activity.
                    self.activityTimer = 1                                                                                  # Reset the timer to 1.
                    self.activityInteractive = None                                                                 # Reset the interactive to None.
            elif( lowestNeedName == 'water' ):
                if( lowestNeedValue < 833.333333333 ):                                                          # The water need is not below the minimal limit.
                    for object in self.world.objects:
                        if( object.type == 'Refrigerator' ):
                            self.activity = 'drink'
                            self.activityTimer = 60                                                                 # 1 game minute.
                            self.activityInteractive = object.id
                            if( self.isInRange( object, 'NextTo' ) == False ):
                                self.goTo( object.pos[0], object.pos[1], object.pos[2] )
                                self.move()
                else:                                                                                                                           # The lowest need is not below the minimal limit.
                    self.activity = 'beHappy'                                                                               # Reset the activity to a standard beHappy activity.
                    self.activityTimer = 1                                                                                  # Reset the timer to 1.
                    self.activityInteractive = None                                                                 # Reset the interactive to None.
            elif( lowestNeedName == 'hygiene' ):
                if( lowestNeedValue < 833.333333333 ):                                                          # The hygiene need is not below the minimal limit.
                    for object in self.world.objects:
                        if( object.type == 'Shower' ):
                            self.activity = 'shower'
                            self.activityTimer = 1800                                                               # 30 game minutes.
                            self.activityInteractive = object.id
                            if( self.isInRange( object, 'On' ) == False ):
                                self.goTo( object.pos[0], object.pos[1], object.pos[2] )
                                self.move()
                else:                                                                                                                           # The lowest need is not below the minimal limit.
                    self.activity = 'beHappy'                                                                               # Reset the activity to a standard beHappy activity.
                    self.activityTimer = 1                                                                                  # Reset the timer to 1.
                    self.activityInteractive = None                                                                 # Reset the interactive to None.
            elif( lowestNeedName == 'fun' ):
                if( lowestNeedValue < 833.333333333 ):
                    for object in self.world.objects:
                        if( object.type == 'TvSet' ):
                            self.activity = 'watch'
                            self.activityTimer = 1800   # 30 game minutes.
                            self.activityInteractive = object.id
                            if( self.isInRange( object, 'On' ) == False ):
                                # If the character is not in range set the new destination and move to it.
                                self.goTo( object.pos[0], object.pos[1], object.pos[2] )
                                self.move()
                else:                                   # The lowest need is not below the minimal limit.
                    self.activity = 'beHappy'           # Reset the activity to a standard beHappy activity.
                    self.activityTimer = 1              # Reset the timer to 1.
                    self.activityInteractive = None     # Reset the interactive to None.
            else:                                       # There is no lowest need. Should never happen.
                self.activity = 'beHappy'               # Reset the activity to a standard beHappy activity.
                self.activityTimer = 1                  # Reset the timer to 1.
                self.activityInteractive = None         # Reset the interactive to None.
