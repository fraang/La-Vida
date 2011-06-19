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

class lv_object:
	# The base class for in world objects. Every real in world object is an sub class of the lv_object class.
	def __init__( self, id ):
		self.id = id
		self.type = 'generic'
		self.pos = [ 0, 0, 0 ]
		self.isInUse = False
