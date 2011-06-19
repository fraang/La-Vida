#!/usr/bin/python
#*** encoding:utf-8 ***

from twisted.internet import protocol

from lv_protocol import lv_protocol

class lv_serverFactory( protocol.ServerFactory ):
	protocol = lv_protocol
