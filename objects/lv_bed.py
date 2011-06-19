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
