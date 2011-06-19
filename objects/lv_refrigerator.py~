#!/usr/bin/python
#*** encoding:utf-8 ***

import gameEngine
from gameEngine.lv_object import lv_object

class lv_refrigerator( lv_object ):
	def __init__( self, id, x, y, z ):
		self.id = id
		self.type = 'refrigerator'
		self.pos = [ x, y, z ]
		self.isInUse = False
		
	def drink( self, user ):
		# The user drinks somthing.
		print 'DEBUG: lv_refrigerator::drink is called.'
		user.increaseNeed( 'water', 1.388888889 )
		
	def eatSnack( self, user ):
		# The user eats a snack.
		print 'DEBUG: lv_refrigerator::eatSnack is called.'
		user.increaseNeed( 'food', 0.555555556 )
