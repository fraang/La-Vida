#!/usr/bin/python
#*** encoding:utf-8 ***

import gameEngine
from gameEngine.lv_object import lv_object

class lv_bed( lv_object ):
	def __init__( self, id, x, y, z ):
		self.id = id
		self.type = 'bed'
		self.pos = [ x, y, z ]
		self.isInUse = False

	def rest( self, user ):
		# The user rests on the bed.
		print 'DEBUG: lv_bed::rest is called.'
		user.increaseNeed( 'sleep', 0.008680555 )
		
	def sleep( self, user ):
		# The user sleeps on the bed.
		print 'DEBUG: lv_bed::sleep is called.'
		user.increaseNeed( 'sleep', 0.034722222 )
