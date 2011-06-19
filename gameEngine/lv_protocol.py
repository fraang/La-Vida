#!/usr/bin/python
#*** encoding:utf-8 ***

from twisted.protocols import basic

class lv_protocol( basic.LineReceiver ):
	def lineReceived( self, line ):
		if( line == "stop" ):
			self.sendLine("server_stoped")
			reactor.stop()
