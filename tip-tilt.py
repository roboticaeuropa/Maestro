#!/usr/bin/python

import time
import maestro as m

# Definicion de canales
azimuth=2
elevation=3
left=4
right=5 

# Definicion de rangos
min=3500
zero=5000
max=12500

# Definicion de ejes
moving= azimuth
resting= elevation

s= m.Controller()

while (1):
	s.setTarget(moving,min)
	s.setTarget(resting,zero)
	time.sleep(1)

	s.setTarget(moving,zero)
	s.setTarget(resting,zero)
	time.sleep(1)

	s.setTarget(moving,max)
	s.setTarget(resting,zero)
	time.sleep(1)

	s.setTarget(moving,zero)
	s.setTarget(resting,zero)
	time.sleep(1)

s.setTarget(moving,min)
s.setTarget(resting,zero)
time.sleep(1)
