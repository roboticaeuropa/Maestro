#!/usr/bin/python

import time
import maestro as m
s= m.Controller()

zero=6000
correc   = -0.16

print "==== ACELERACION ===="
speed=400 # Velocidad de puesta en marcha
desv= int(round(speed*correc,0))
print "speed=",speed
print "desv=",desv
# ===========================
speed_left=zero+(speed+desv)
speed_right=zero-(speed-desv)
print "speed_left",speed_left
print "speed_right",speed_right

s.setTarget(4,speed_left) #,-1) These motors have the same direction of rotation
s.setTarget(5,speed_right) #,1)
time.sleep(0.5) # ======= Tiempo de puesta en marcha

print "==== VELOCIDAD MAXIMA ===="
speed=800 # Velocidad de puesta en marcha
desv= int(round(speed*correc,0))
print "speed=",speed
print "desv=",desv
# ===========================
speed_left=zero+(speed+desv)
speed_right=zero-(speed-desv)
print "speed_left",speed_left
print "speed_right",speed_right

s.setTarget(4,speed_left) #,-1) These motors have the same direction of rotation
s.setTarget(5,speed_right) #,1)
time.sleep(5) # ======= Tiempo de recorrido

s.setTarget(4,0)
s.setTarget(5,0)

