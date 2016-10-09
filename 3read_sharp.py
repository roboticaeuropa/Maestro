#!/usr/bin/python

import time
import maestro as m

# Crear objeto MicroMaestro
s= m.Controller()

# Asignacion de canales
sharp=0

# Lecturas de distancia a obstaculo antes de arrancar
iter=1
while (1):
	pos_ini_min=s.getPosition(sharp)
	pos_ini_max=s.getPosition(sharp)
	print "ITERACION ",iter
	iter=iter+1
        print "sensing..."
        time.sleep(1.5)
	print "Distancia (min)=",pos_ini_min
	print "Distancia (man)=",pos_ini_max
	print ""
