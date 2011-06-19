#!/usr/bin/python
#*** encoding:utf-8 ***

import gameEngine
from gameEngine.lv_object import lv_object

class lv_shower( lv_object ):
	def __init__( self, id, x, y, z ):
		self.id = id
		self.type = 'shower'
		self.pos = [ x, y, z ]
		self.isInUse = False
		
	def takeAShower( self, user ):
		# The user takes a  shower.
		print 'DEBUG: lv_shower::takeAsShower is called.'
		user.increaseNeed( 'hygiene', 0.555555556 )
