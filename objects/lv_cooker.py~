#!/usr/bin/python
#*** encoding:utf-8 ***

import gameEngine
from gameEngine.lv_object import lv_object

class lv_cooker( lv_object ):
	def __init__( self, id, x, y, z ):
		self.id = id
		self.type = 'cooker'
		self.pos = [ x, y, z ]
		self.isInUse = False
		
	def cook( self, user ):
		# The user cooks on the cooker and eats.
		print 'DEBUG: lv_cooker::cook is called.'
		user.increaseNeed( 'food', 0.37037037 )
