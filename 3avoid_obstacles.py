#!/usr/bin/python

import time
import maestro as m

# Crear objeto MicroMaestro
s= m.Controller()

# Asignacion de canales
sharp = 0
servo_izq = 4
servo_dcho = 5

# Distancia de evitacion (600 choque, 0 sin obstaculo)
obstacle_alarm= 250

# Tiempos de movimiento y pausa para estabilizacion de lectura
avance = 0.5
turning = 0.75
stopped= 0.5

# Lecturas de distancia a obstaculo antes de arrancar
iter=1
while (1):
	pos_min=s.getPosition(sharp)
	pos_max=s.getPosition(sharp)
	pos=0.5*(pos_min+pos_max)
	print "ITERACION ",iter
	iter=iter+1
	print "Distancia (600-0)=",pos
	if pos > obstacle_alarm:
		print "Me paro pq hay obstaculo"
                time.sleep(stopped)
		print "Rotando para evitar obstaculo"
		s.setTarget(4,1)
		s.setTarget(5,-1)
        	time.sleep(turning)
                s.setTarget(4,0)
                s.setTarget(5,0)
		time.sleep(stopped)

	else:
		s.setTarget(4,1)
		s.setTarget(5,1)
		print ""
		print ""
	time.sleep(avance)
