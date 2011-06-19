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
from time import sleep, time
from ConfigParser import ConfigParser

import gameEngine
from gameEngine.lv_character import lv_character

import objects
from objects.lv_bed import lv_bed
from objects.lv_cooker import lv_cooker
from objects.lv_refrigerator import lv_refrigerator
from objects.lv_shower import lv_shower

class lv_world:
	def __init__( self, amountOfCharacters ):
		# Basic infrastructure
		self.configParser = ConfigParser()
		
		# Reading the game engine cinfiguration
		if( os.path.exists( '../config/gameEngine.cfg' ) == True ):
			self.configParser.read( open( '../config/gameEngine.cfg' ) )
			self.gameEngineConfigExists = True
		else:
			self.gameEngineConfigExists = False
			print '\033[31mError\033[0m No game engine configuration file found. Using default options.'
		
		# Game time
		self.startTime			= time()	# The start time
		self.gameYear			= 1		# In game year; NOT real year
		self.gameMonth			= 1		# In game month; NOT real month
		self.gameDay			= 1		# In game day; NOT real day
		self.gameHour			= 0		# In game hour; NOT real hour
		self.gameMinute			= 0		# In game minute; NOT real minute
		self.gameSecond			= 0		# In game second; NOT real second
		
		if( self.gameEngineConfigExists == True ):
			self.ticksPerSecond	= self.configParser.get( 'time', 'ticksPerSecond' )	# Ticks per second
			self.gameSecondsPerTick	= self.configParser.get( 'time', 'gameSecondsPerTick' )	# The amount of game seconds passing each tick
		else:
			self.ticksPerSecond	= 25
			self.gameSecondsPerTick	= 1
		
		# Physics data
		self.physicsGravity		= 9.8		# Factor of gravity
		
		# Terrain information
		self.typeMap			= []		# Type of the ground
		self.heightMap			= []		# Height of the ground
		
		# Entities in the world
		self.characters			= []		# List of characters in the world
		self.objects			= []		# List of objects in the world

		for i in range(amountOfCharacters):
			self.characters.insert( 0, lv_character( i, self, 'random' ) )

		self.objects.insert( 0, lv_bed( 0, 1, 1, 0 ) )
		self.objects.insert( 1, lv_cooker( 1, 1, 1, 0 ) )
		self.objects.insert( 2, lv_refrigerator( 2, 1, 1, 0 ) )
		self.objects.insert( 3, lv_shower( 3, 1, 1, 0 ) )
		
	def processTime( self ):
		# Process the game time.
		self.gameSecond += self.gameSecondsPerTick
		if( self.gameSecond >= 60 ):
			self.gameMinute += 1
			self.gameSecond = 0
			
		if( self.gameMinute >= 60 ):
			self.gameHour += 1
			self.gameMinute = 0
			
		if( self.gameHour >= 24 ):
			self.gameDay += 1
			self.gameHour = 0
			
		if( self.gameMonth == 1 or self.gameMonth == 3 or self.gameMonth == 5 or self.gameMonth == 7 or self.gameMonth == 8 or self.gameMonth == 10 or self.gameMonth >= 12 ):
			if( self.gameDay == 32 ):
				self.gameMonth += 1
				self.gameDay = 1
		elif( self.gameMonth == 2 ):
			if( self.gameYear % 4 == 0 ):
				if( self.gameDay == 30 ):
					self.gameMonth += 1
					self.gameDay = 1
			else:
				if( self.gameDay == 29 ):
					self.gameMonth += 1
					self.gameDay = 1
		elif( self.gameMonth == 4 or self.gameMonth == 6 or self.gameMonth == 9 or self.gameMonth == 11 ):
			if( self.gameDay == 31 ):
				self.gameMonth += 1
				self.gameDay = 1
			
		if( self.gameMonth >= 13 ):
			self.gameYear += 1
			self.gameMonth = 1
	
	def processGravity( self ):
		# Processes gravity on characters and objects.
		for character in self.characters:
			if( character.pos[2] > 0):
				character.pos[2] -= 1
			else:
				character.pos[2] = 0
		for object in self.objects:
			if( object.pos[2] > 0):
				object.pos[2] -= 1
			else:
				object.pos[2] = 0
			
	def run( self ):
		while( self.gameDay <= 7 ):
			os.system('clear')
			self.processTime()
			self.processGravity()
			print '\033[32mInfo\033[0m World     Game date: %i-%i-%i\tGame time: %i:%i:%i' % ( self.gameYear, self.gameMonth, self.gameDay, self.gameHour, self.gameMinute, self.gameSecond )
			for character in self.characters:
				print '\033[32mInfo\033[0m Character %i, %s' % ( character.id, character.gender )
				print '\033[32mInfo\033[0m           Sleep: %i\tFood: %i\tWater: %i' % ( character.needs['sleep'], character.needs['food'], character.needs['water'] )
				print '\033[32mInfo\033[0m           Hygiene: %i\tFun: %i\tSocial: %i' % ( character.needs['hygiene'], character.needs['fun'], character.needs['social'] )
				print '\033[32mInfo\033[0m           Activity: %s (%i game seconds left)' % ( character.activity, character.activityTimer )
				character.decreaseNeeds()
				character.processActivity()
			sleep( 1 / self.ticksPerSecond )
