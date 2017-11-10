#!/usr/bin/python
# -*- coding: utf-8 -*-

import Pyro4
from scbl import BufferLimitado

b = BufferLimitado()

@Pyro4.expose
class Semaforo(object):
	def produzir(self, item):
		self.item = item
		b.insert(self.item)
		print "PRODUTOR. item: ", self.item
		return (str(item))

	def consumir(self):
		self.item = b.remove()
		print " CONSUMIDOR. item: ", self.item
		return (str(self.item))

Pyro4.Daemon.serveSimple({Semaforo: "Semaforo"})
print "Server conectado..."