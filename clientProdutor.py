#!/usr/bin/python
# -*- coding: utf-8 -*-

import Pyro4

Semaforo = Pyro4.Proxy("PYRONAME:exemplo.consumo")
print "Produtor conectado..."

print(Semaforo.produzir())


