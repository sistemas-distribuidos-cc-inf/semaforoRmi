#!/usr/bin/python
# -*- coding: utf-8 -*-

import Pyro4
from scbl import BufferLimitado

b = BufferLimitado()

@Pyro4.expose
class Semaforo(object):
	def produzir(item):
	    b.insert(item)
	    print "PRODUTOR. item: ", item , " b.livre: ", b.livre, " b.cheio: ", b.cheio
	    return (str(item))

	def consumir(item):
	    item = b.remove()
	    print " CONSUMIDOR. item: ", item , " b.livre: ", b.livre, " b.cheio: ",  b.cheio
	    return (str(item))

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = daemon.register(Semaforo)
#uri = daemon.register(Consumo)
ns.register("exemplo.consumo",uri)

print "Server conectado..."
daemon.requestLoop()
