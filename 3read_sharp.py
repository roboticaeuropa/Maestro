#!/usr/bin/python

import time
import maestro as m

# Crear objeto MicroMaestro
s= m.Controller()

# Asignacion de canales
sharp=0

# Parametros de la ecuacion Voltaje-Distancia
A= 5788
B= 8.44
C= 0.89

# Lecturas de distancia a obstaculo antes de arrancar
iter=1
while (1):
	pos_ini_min=s.getPosition(sharp)
	pos_ini_max=s.getPosition(sharp)
	dis_ini_min = A/(pos_ini_min-B)-C
        dis_ini_max = A/(pos_ini_max-B)-C
	print "ITERACION ",iter
	iter=iter+1
        print "sensing..."
        time.sleep(0.5)
	print "Voltaje (min)=",pos_ini_min
	print "Voltaje (max)=",pos_ini_max
	print "--------------"
	print "Distancia (min)=",dis_ini_min,"cm"
	print "Distancia (max)=",dis_ini_max,"cm"
