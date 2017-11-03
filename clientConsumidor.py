#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import Pyro4

Semaforo = Pyro4.Proxy("PYRONAME:exemplo.consumo")
print "Consumidor conectado..."

print(Semaforo.consumir())
