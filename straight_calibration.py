#!/usr/bin/python

import time
import maestro as m
s= m.Controller()

zero=6000
speed=800

miles   = 0.15

desv= int(round(speed*miles,0))
print "desv=",desv
speed_desv=speed+desv

speed_left=zero+speed_desv
speed_right=zero-speed_desv
print "speed_left",speed_left
print "speed_right",speed_right


s.setTarget(4,speed_left) #,-1)
s.setTarget(5,speed_right) #,1)

time.sleep(10)

s.setTarget(4,0)
s.setTarget(5,0)

