#!/usr/bin/python
# -*- coding: utf-8 -*-

import Pyro4

objRemotoSemaforo = Pyro4.Proxy("PYRONAME:Semaforo")

while 1: objRemotoSemaforo.produzir(1111)



