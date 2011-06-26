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

class Brain:
    # The brain class provides attributes and methodes for the ai of an character.
    
    def __init__( self, character ):
        self.character = character
        self.activitiesHigh = { 'sleep': 'rest',
                                'food': 'eatSnack',
                                'water': 'drink',
                                'urination': 'use',
                                'hygiene': 'shower',
                                'fun': 'watch',
                                'social': 'talk' }
        self.activitiesMedium = { 'sleep': 'rest',
                                  'food': 'cook',
                                  'water': 'drink',
                                  'urination': 'use',
                                  'hygiene': 'shower',
                                  'fun': 'watch',
                                  'social': 'talk' }
        self.activitiesLow = { 'sleep': 'sleep',
                               'food': 'cook',
                               'water': 'drink',
                               'urination': 'use',
                               'hygiene': 'shower',
                               'fun': 'watch',
                               'social': 'talk' }
        self.activityTimes = { 'rest': 900,
                               'sleep': 28800,
                               'eatSnack': 300,
                               'cook': 900,
                               'drink': 60,
                               'use': 450,
                               'shower': 1800,
                               'watch': 1800,
                               'talk': 300 }
        self.activityInteractiveTypes = { 'rest': 'Bed',
                                          'sleep': 'Bed',
                                          'eatSnack': 'Refrigerator',
                                          'cook': 'Cooker',
                                          'drink': 'Refrigerator',
                                          'use': 'Toilet',
                                          'shower': 'Shower',
                                          'watch': 'TvSet',
                                          'talk': 'Character' }
        self.activity = None
        self.activityTimer = 0
        self.activityInteractive = None
        
    def getLowestNeed( self ):
        # Returns the lowest need including its value as a tuple.
        lowestNeed = (None, 1000)
        for need in self.character.needs.keys():
            try:
                if( self.character.needs[need] < lowestNeed[1] ):
                    lowestNeed = ( need, self.character.needs[need] )
            except:
                print '\033[31mError\033[0m Character: %i\tNeed %s does not exist.' % ( self.character.id, need )
        return lowestNeed
        
    def getHighestNeed( self ):
        # Returns the highest need including its value as a tuple.
        highestNeed = (None, 0)
        for need in self.character.needs.keys():
            try:
                if( self.character.needs[need] > highestNeed[1] ):
                    highestNeed = ( need, self.character.needs[need] )
            except:
                print '\033[31mError\033[0m Character: %i\tNeed %s does not exist.' % ( self.character.id, need )
        return highestNeed
        
    def getNextActivity( self ):
        # Get the next activity to satisfy the lowest need.
        if( self.getLowestNeed()[1] <= 250 ): # 1/4, Low
            self.activity = self.activitiesLow[ self.getLowestNeed()[0] ]
            self.activityTimer = self.activityTimes[ self.activity ]
            if( self.activityInteractiveTypes[ self.activity ] == 'Character' ):
                self.activityInteractive = self.getCharacterById( 1 )
            else:
                self.activityInteractive = self.getObjectByType( self.activityInteractiveTypes[ self.activity ] )
            return self.activitiesLow[ self.getLowestNeed()[0] ]
        elif( self.getLowestNeed()[1] <= 500 ): # 1/2, Medium
            self.activity = self.activitiesMedium[ self.getLowestNeed()[0] ]
            self.activityTimer = self.activityTimes[ self.activity ]
            if( self.activityInteractiveTypes[ self.activity ] == 'Character' ):
                self.activityInteractive = self.getCharacterById( 1 )
            else:
                self.activityInteractive = self.getObjectByType( self.activityInteractiveTypes[ self.activity ] )
            return self.activitiesMedium[ self.getLowestNeed()[0] ]
        elif( self.getLowestNeed()[1] <= 750 ):   # 3/4, High
            self.activity = self.activitiesHigh[ self.getLowestNeed()[0] ]
            self.activityTimer = self.activityTimes[ self.activity ]
            if( self.activityInteractiveTypes[ self.activity ] == 'Character' ):
                self.activityInteractive = self.getCharacterById( 1 )
            else:
                self.activityInteractive = self.getObjectByType( self.activityInteractiveTypes[ self.activity ] )
            return self.activitiesHigh[ self.getLowestNeed()[0] ]
        else:
            self.activity = None
            self.activityTimer = 0
            self.activityInteractive = None
            return None
            
    def getCharacterById( self, id ):
        # Searches for a character in the world by id and returns it.
        for character in self.character.world.characters:
            if( character.id == id ):
                return character
                
    def getObjectById( self, id ):
        # Searches for an object in the world by id and returns it.
        for object in self.character.world.objects:
            if( object.id == id ):
                return object
                
    def getObjectByType( self, type ):
        # Searches for an object in the world by type and returns it.
        for object in self.character.world.objects:
            if( object.type == type ):
                return object
                
    def isInRange( self, characterOrObject, radiusType ):
        # Checks if a character or object is in range by utilization of a bounding box and returns True if the object is in range.
        try:
            # X axis
            if( self.character.pos[ 0 ] >= characterOrObject.pos[ 0 ] - characterOrObject.radii[ radiusType ] and
                self.character.pos[ 0 ] <= characterOrObject.pos[ 0 ] + characterOrObject.radii[ radiusType ] ):
                # Y axis
                if( self.character.pos[ 1 ] >= characterOrObject.pos[ 1 ] - characterOrObject.radii[ radiusType ] and
                    self.character.pos[ 1 ] <= characterOrObject.pos[ 1 ] + characterOrObject.radii[ radiusType ] ):
                    # Z axis
                    if( self.character.pos[ 2 ] >= characterOrObject.pos[ 2 ] - characterOrObject.radii[ radiusType ] and
                        self.character.pos[ 2 ] <= characterOrObject.pos[ 2 ] + characterOrObject.radii[ radiusType ] ):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        except:
            return False
