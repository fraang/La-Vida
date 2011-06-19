#!/usr/bin/python

import os, random, time, socket

class lv_client:
	def __init__( self ):
		self.socket = socket.socket()
		self.socket.bind( ( '127.0.0.1', 65001 ) )
		print 'lv_client: Client socket data'
		print '           IP address: %s \tPort: %i' % ( self.socket.getsockname()[0], self.socket.getsockname()[1] )
		self.connected = False

	def connect( self ):
		for i in range(10):
			try:
				self.socket.connect( ( '127.0.0.1', 65000 ) )
				self.connected = True
				break
			except:
				print 'lv_client: Unable to connect.'
				# self.connected = False
			time.sleep(1)
			
	def send( self, data ):
		try:
			self.socket.send( '%s' % ( data ) )
		except:
			print 'lv_client: Unable to send data.'
		
	def recieve( self ):
		for i in range(3):
			try:
				print 'lv_client: Recieved data: %s' % ( self.socket.recv( 255 ) )
				break
			except:
				print 'lv_client: Unable to recieve data.'
			time.sleep(1)
			
	def close( self ):
		self.socket.close()

lv_client_test = lv_client()
lv_client_test.connect()
if( lv_client_test.connected == True ):
	lv_client_test.send( 'stop\r\n' )
	lv_client_test.close()
