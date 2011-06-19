#!/usr/bin/python
#*** encoding:utf-8 ***

class lv_object:
	# The base class for in world objects. Every real in world object is an sub class of the lv_object class.
	def __init__( self, id ):
		self.id = id
		self.type = 'generic'
		self.pos = [ 0, 0, 0 ]
		self.isInUse = False
