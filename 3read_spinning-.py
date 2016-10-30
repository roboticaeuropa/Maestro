#!/usr/bin/python

import time
import maestro as m

# Crear objeto MicroMaestro
s= m.Controller()

# Asignacion de canales
sharp=0
servo_izq=4
servo_dcho=5

# Lecturas de distancia a obstaculo antes de arrancar
iter=1
while (1):
	pos_ini_min=s.getPosition(sharp)
	pos_ini_max=s.getPosition(sharp)
	print "ITERACION ",iter
	iter=iter+1
	print "Distancia (min)=",pos_ini_min
	print "Distancia (man)=",pos_ini_max

	s.setTarget(4,1)
	s.setTarget(5,1)
        pos_servo_izq=s.getPosition(servo_izq)
        pos_servo_dcho=s.getPosition(servo_dcho)
        print "Posicion servo izquierdo=",pos_servo_izq
        print "Posicion servo derecha=",pos_servo_dcho
	time.sleep(2)

	s.setTarget(4,0)
	s.setTarget(5,0)
        pos_servo_izq=s.getPosition(servo_izq)
        pos_servo_dcho=s.getPosition(servo_dcho)
        print "Posicion servo izquierdo=",pos_servo_izq
        print "Posicion servo derecha=",pos_servo_dcho
	print ""
	time.sleep(2)
