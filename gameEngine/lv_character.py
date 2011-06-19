#!/usr/bin/python
#*** encoding:utf-8 ***

from random import choice

class lv_character:
	def __init__( self, id, world, gender ):
		self.id = id
		self.world = world
		self.pos = [ 0, 0, 0 ]
		
		if( gender.lower() == 'random' ):
			self.gender = choice( ( 'male', 'female' ) )
		else:
			self.gender = gender
		
		self.activity = None
		self.activityTimer = 0
		self.activityInteractive = None
		
		self.needs = {	'sleep':	1000,
						'food':		1000,
						'water':	1000,
						'hygiene':	1000,
						'fun':		1000,
						'social':	1000 }
	
	def move( self, x, y, z ):
		self.pos = [ x, y, z ]
		
	def isInRange( self, characterOrObject ):
		if( characterOrObject.pos[ 0 ] >= self.pos[ 0 ] - 5 and characterOrObject.pos[0] <= self.pos[ 0 ] + 5 ):
			if( characterOrObject.pos[ 1 ] >= self.pos[ 1 ] - 5 and characterOrObject.pos[ 1 ] <= self.pos[ 1 ] + 5 ):
				if( characterOrObject.pos[ 2 ] >= self.pos[ 2 ] - 5 and characterOrObject.pos[ 2 ] <= self.pos[ 2 ] + 5 ):
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
			if( self.activity != 'takeAShower' ):
				self.needs['hygiene'] -= 0.005787037
			# if( self.activity != 'watchTV' ):
			#	self.needs['fun'] -= 1
			# if( self.activity != 'chat' ):
			#	self.needs['social'] -= 1
		except:
			pass
			
	def processActivity( self ):
		# Process the activity of a character.
		if( self.activityTimer > 0 ):												# Character has active activity.
			print 'Character is doing activity. Timer is not zero.'
			objectFound = False
			for object in self.world.objects:										# Search for the object to interact with.
				if( object.id == self.activityInteractive ):						# Object found in the wolrd's object list.
					objectFound = True
					if( self.isInRange( object ) ):									# Checks if the object is in range of the character.
						print 'Object found to interact with and is in range. Object id is %i/%i.' % ( self.activityInteractive, object.id )
						print 'Character interacts with the object of type %s.' % ( object.type )
						exec 'object.%s( self )' % ( self.activity )				# Calls the methode of an world object which
																					# triggers a callback of a characters methode to
																					# modify a character attribute.
						self.activityTimer -= 1
					else:
						print 'Object found to interact with but is not in range. Object id is %i/%i.' % ( self.activityInteractive, object.id )
						self.move( object.pos[0], object.pos[1], object.pos[2] )
			if( objectFound == False ):												# Object not found in the world's object list.
				print 'Object not found to interact. Object id is %s/%i.' % ( self.activityInteractive, object.id )
				self.activity = None
				self.activityTimer = 0
				self.activityInteractive = None
		else:																		# Character is free for a new activity.
			print 'Character is thinking about the next activity. Timer is zero.'
			# Getting the lowest need
			lowestNeedName	= ''
			lowestNeedValue	= 1000
			for needName in self.needs.keys():
				if( self.needs.get( needName ) < lowestNeedValue ):
					lowestNeedName	= needName
					lowestNeedValue	= self.needs.get( needName )

			print 'The lowest need is %s with a value of %i.' % ( lowestNeedName, lowestNeedValue )
						
			# Searching for an character or object to raise the need
			# if( lowestNeedName == 'fun' or lowestNeedName == 'social' ):
			#	for character in self.world.characters:
			#		self.needs[lowestNeedName] = 1000
			#		# if( character. ):
			if( lowestNeedName == 'sleep' ):
				if( lowestNeedValue < 833.333333333 ):								# The sleep need is not below the minimal limit.
					for object in self.world.objects:								# Search for the object to interact with.
						if( object.type == 'bed' ):									# Object of type bed found in the wolrd's object list.
							if( lowestNeedValue > 208.333333333 ):					# The sleep need is not below the critcal limit.
								self.activity = 'rest'
								self.activityTimer = 900							# 15 game minutes
								self.activityInteractive = object.id
							else:													# The sleep need is below the critcal limit.
								self.activity = 'sleep'
								self.activityTimer = 28800							# 8 game hours
								self.activityInteractive = object.id
				else:																# The lowest need is not below the minimal limit.
					self.activity = 'beHappy'										# Reset the activity to a standard beHappy activity.
					self.activityTimer = 1											# Reset the timer to 1.
					self.activityInteractive = None									# Reset the interactive to None.
			elif( lowestNeedName == 'food' ):
				if( lowestNeedValue < 833.333333333 ):								# The food need is not below the minimal limit.
					for object in self.world.objects:								# Search for the object to interact with.
						if( object.type == 'refrigerator' ):						# Object of type refrigerator found in the wolrd's object list.
							if( lowestNeedValue > 833.333333333 ):					# The food need is not below the critcal limit.
								self.activity = 'eatSnack'
								self.activityTimer = 300							# 5 game minutes.
								self.activityInteractive = object.id				
						elif( object.type == 'cooker' ):							# Object of type cooker found in the wolrd's object list.
							if( lowestNeedValue > 0 ):								# The food need is below the critcal limit.
								self.activity = 'cook'
								self.activityTimer = 900							# 15 game minutes.
								self.activityInteractive = object.id
				else:																# The lowest need is not below the minimal limit.
					self.activity = 'beHappy'										# Reset the activity to a standard beHappy activity.
					self.activityTimer = 1											# Reset the timer to 1.
					self.activityInteractive = None									# Reset the interactive to None.
			elif( lowestNeedName == 'water' ):
				if( lowestNeedValue < 833.333333333 ):								# The water need is not below the minimal limit.
					for object in self.world.objects:
						if( object.type == 'refrigerator' ):
							self.activity = 'drink'
							self.activityTimer = 60									# 1 game minute.
							self.activityInteractive = object.id
				else:																# The lowest need is not below the minimal limit.
					self.activity = 'beHappy'										# Reset the activity to a standard beHappy activity.
					self.activityTimer = 1											# Reset the timer to 1.
					self.activityInteractive = None									# Reset the interactive to None.
			elif( lowestNeedName == 'hygiene' ):
				if( lowestNeedValue < 833.333333333 ):								# The hygiene need is not below the minimal limit.
					for object in self.world.objects:
						if( object.type == 'shower' ):
							self.activity = 'takeAShower'
							self.activityTimer = 1800								# 30 game minutes.
							self.activityInteractive = object.id
				else:																# The lowest need is not below the minimal limit.
					self.activity = 'beHappy'										# Reset the activity to a standard beHappy activity.
					self.activityTimer = 1											# Reset the timer to 1.
					self.activityInteractive = None									# Reset the interactive to None.
			else:
				self.activity = 'beHappy'											# Reset the activity to a standard beHappy activity.
				self.activityTimer = 1												# Reset the timer to 1.
				self.activityInteractive = None										# Reset the interactive to None.
